from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from core.utils import SearchBarView
from fullweb.income.forms import IncomeCreateForm, IncomeEditForm, IncomeDeleteForm
from fullweb.income.models import Income
from django.contrib.auth import mixins


class ListIncomeView(mixins.LoginRequiredMixin, SearchBarView):
    template_name = 'income/income-list.html'
    model = Income


class CreateIncomeView(mixins.LoginRequiredMixin, views.CreateView):
    model = Income
    template_name = 'income/income-create.html'
    form_class = IncomeCreateForm

    def form_valid(self, form):
        income=form.save(commit=False)
        income.user = self.request.user
        self.object = income.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('income list')


@login_required
def edit_income(request, income_pk):

    income = Income.objects.get(pk=income_pk)

    if request.method == "GET":
        form = IncomeEditForm(instance=income)
    else:
        form = IncomeEditForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect('income list')

    context = {
        'form':form,
        'income_pk': income_pk
    }

    return render(request, 'income/income-edit.html', context=context)


@login_required
def delete_income(request, income_pk):

    if request.user.is_staff and not request.user.is_superuser:
        return redirect('income list')

    income = Income.objects.get(pk=income_pk)

    form = IncomeDeleteForm(instance=income)
    if request.method == "POST":
        income.delete()
        return redirect('income list')

    context = {
        'form': form,
        'income_pk': income_pk
    }

    return render(request, 'income/income-delete.html', context=context)