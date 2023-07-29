from django import forms
from fullweb.bills.models import Bill


class BillBaseForm(forms.ModelForm):

    class Meta:
        model = Bill
        fields = ['date', 'description', 'amount']

        labels = {
            'date': 'Bill date'
        }

        widgets = {
            'date': forms.DateInput(
                attrs= {
                    'placeholder': 'Date',
                    'type': 'date',
                },
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Description'
                },
            ),
            'amount': forms.NumberInput(
                attrs={
                    'placeholder': 'Amount'
                },
            ),
        }


class BillCreateForm(BillBaseForm):
    pass


class BillEditForm(BillBaseForm):
    pass


class BillDeleteForm(BillBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'
