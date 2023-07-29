from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from core.utils import SearchBarView
from fullweb.other.forms import OtherCreateForm, OtherEditForm, OtherDeleteForm
from fullweb.other.models import Other
from django.contrib.auth import mixins


class ListOtherView(mixins.LoginRequiredMixin, SearchBarView):
    template_name = 'other/other-list.html'
    model = Other


class CreateOtherView(mixins.LoginRequiredMixin, views.CreateView):
    model = Other
    template_name = 'other/other-create.html'
    form_class = OtherCreateForm

    def form_valid(self, form):
        other=form.save(commit=False)
        other.user = self.request.user
        self.object = other.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('other list')


@login_required
def edit_other(request, other_pk):

    other = Other.objects.get(pk=other_pk)

    if request.method == "GET":
        form = OtherEditForm(instance=other)
    else:
        form = OtherEditForm(request.POST, instance=other)
        if form.is_valid():
            form.save()
            return redirect('other list')

    context = {
        'form':form,
        'other_pk': other_pk
    }

    return render(request, 'other/other-edit.html', context=context)


@login_required
def delete_other(request, other_pk):

    if request.user.is_staff and not request.user.is_superuser:
        return redirect('other list')

    other = Other.objects.get(pk=other_pk)

    form = OtherDeleteForm(instance=other)
    if request.method == "POST":
        other.delete()
        return redirect('other list')

    context = {
        'form': form,
        'other_pk': other_pk
    }

    return render(request, 'other/other-delete.html', context=context)