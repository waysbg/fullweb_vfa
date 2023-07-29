from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from core.utils import SearchBarView
from fullweb.bills.forms import BillCreateForm, BillEditForm, BillDeleteForm
from fullweb.bills.models import Bill
from django.contrib.auth import mixins


class ListBillsView(mixins.LoginRequiredMixin, SearchBarView):
    template_name = 'bills/bills-list.html'
    model = Bill


class CreateBillView(mixins.LoginRequiredMixin, views.CreateView):
    model = Bill
    template_name = 'bills/bill-create.html'
    form_class = BillCreateForm

    def form_valid(self, form):
        bill=form.save(commit=False)
        bill.user = self.request.user
        self.object = bill.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('bills list')


@login_required
def edit_bill(request, bill_pk):

    bill = Bill.objects.get(pk=bill_pk)

    if request.method == "GET":
        form = BillEditForm(instance=bill)
    else:
        form = BillEditForm(request.POST, instance=bill)
        if form.is_valid():
            form.save()
            return redirect('bills list')

    context = {
        'form':form,
        'bill_pk': bill_pk
    }

    return render(request, 'bills/bill-edit.html', context=context)


@login_required
def delete_bill(request, bill_pk):

    if request.user.is_staff and not request.user.is_superuser:
        return redirect('bills list')

    bill = Bill.objects.get(pk=bill_pk)

    form = BillDeleteForm(instance=bill)
    if request.method == "POST":
        bill.delete()
        return redirect('bills list')

    context = {
        'form': form,
        'bill_pk': bill_pk
    }

    return render(request, 'bills/bill-delete.html', context=context)