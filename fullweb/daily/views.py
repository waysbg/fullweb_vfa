from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from core.utils import SearchBarView
from fullweb.daily.forms import DailyCreateForm, DailyEditForm, DailyDeleteForm
from fullweb.daily.models import Daily
from django.contrib.auth import mixins


class ListDailyView(mixins.LoginRequiredMixin, SearchBarView):
    template_name = 'daily/daily-list.html'
    model = Daily


class CreateDailyView(mixins.LoginRequiredMixin, views.CreateView):
    model = Daily
    template_name = 'daily/daily-create.html'
    form_class = DailyCreateForm

    def form_valid(self, form):
        daily=form.save(commit=False)
        daily.user = self.request.user
        self.object = daily.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('daily list')


@login_required
def edit_daily(request, daily_pk):

    daily = Daily.objects.get(pk=daily_pk,)

    if request.method == "GET":
        form = DailyEditForm(instance=daily)
    else:
        form = DailyEditForm(request.POST, instance=daily)
        if form.is_valid():
            form.save()
            return redirect('daily list')

    context = {
        'form':form,
        'daily_pk': daily_pk
    }

    return render(request, 'daily/daily-edit.html', context=context)


@login_required
def delete_daily(request, daily_pk):

    if request.user.is_staff and not request.user.is_superuser:
        return redirect('daily list')

    daily = Daily.objects.get(pk=daily_pk)

    form = DailyDeleteForm(instance=daily)
    if request.method == "POST":
        daily.delete()
        return redirect('daily list')

    context = {
        'form': form,
        'daily_pk': daily_pk
    }

    return render(request, 'daily/daily-delete.html', context=context)