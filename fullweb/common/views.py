from datetime import timedelta
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from fullweb.bills.models import Bill
from fullweb.common.utils import percent_factor, bar_length
from fullweb.daily.models import Daily
from fullweb.income.models import Income
from fullweb.other.models import Other

UserModel = get_user_model()


def index(request):

    if request.user.is_authenticated and not request.user.is_staff:
        total_income = sum(income.amount for income in Income.objects.filter(user_id=request.user.pk))
        total_bills = sum(bill.amount for bill in Bill.objects.filter(user_id=request.user.pk))
        total_daily = sum(expense.amount for expense in Daily.objects.filter(user_id=request.user.pk))
        total_other = sum(expense.amount for expense in Other.objects.filter(user_id=request.user.pk))
    else:
        total_income = sum(income.amount for income in Income.objects.all())
        total_bills = sum(bill.amount for bill in Bill.objects.all())
        total_daily = sum(expense.amount for expense in Daily.objects.all())
        total_other = sum(expense.amount for expense in Other.objects.all())

    total_savings = total_income - total_bills - total_daily - total_other

    total_users = UserModel.objects.all().count()

    if total_income == 0:
        total_income += 0.01

    biggest_percent_influencer = max(total_income, total_bills, total_daily, total_other, total_savings)

    total_users_percent = percent_factor(total_users)

    total_income_percent = int(total_income / biggest_percent_influencer * 100)
    total_bills_percent = int(total_bills / biggest_percent_influencer * 100)
    total_daily_percent = int(total_daily / biggest_percent_influencer * 100)
    total_other_percent = int(total_other / biggest_percent_influencer * 100)
    total_savings_percent = int(total_savings / biggest_percent_influencer * 100)

    context = {
        'total_users': total_users,
        'total_income': total_income,
        'total_bills': total_bills,
        'total_daily': total_daily,
        'total_other': total_other,
        'total_savings': total_savings,
        'bar_percent_users': total_users_percent,
        'percent_income': total_income_percent,
        'percent_bills': total_bills_percent,
        'percent_daily': total_daily_percent,
        'percent_other': total_other_percent,
        'percent_savings':total_savings_percent,
        'bar_percent_income': bar_length(total_income_percent),
        'bar_percent_bills': bar_length(total_bills_percent),
        'bar_percent_daily': bar_length(total_daily_percent),
        'bar_percent_other': bar_length(total_other_percent),
        'bar_percent_savings': bar_length(total_savings_percent),
        'show_footer_p': True,
        'show_admin_site': request.user.is_staff,
        'user_is_authenticated': request.user.is_authenticated,
    }

    return render(request, 'common/index.html', context=context)


def important(request):
    context = {
        'show_footer_p': True,
        'show_admin_site': request.user.is_staff,
    }
    return render(request, 'common/important.html', context=context)


@login_required()
def staff_section(request):
    if request.user.is_staff:

        old_users = UserModel.objects.filter(last_login__lt=(timezone.now() - timedelta(365))).order_by('last_login')

        context = {
            'show_footer_p': True,
            'show_admin_site': request.user.is_staff,
            'old_users':old_users,
            'old_users_count': old_users.count(),
        }

        return render(request, 'common/staff-section.html', context=context)
    else:
        return redirect('index')


@login_required
def users_delete(request):

    if request.user.is_staff:

        old_users = UserModel.objects.filter(last_login__lt=(timezone.now() - timedelta(365)))

        if request.method == "POST":
            old_users.delete()
            return redirect('admin site')

        context = {
            'show_footer_p': True,
            'show_admin_site': request.user.is_staff,
        }

        return render(request, 'common/users-delete.html', context=context)

    else:
        return redirect('index')

