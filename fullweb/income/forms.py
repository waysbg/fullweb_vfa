from django import forms

from fullweb.income.models import Income


class IncomeBaseForm(forms.ModelForm):

    class Meta:
        model = Income
        fields = ['date', 'description', 'amount']

        labels = {
            'date': 'Income date'
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


class IncomeCreateForm(IncomeBaseForm):
    pass


class IncomeEditForm(IncomeBaseForm):
    pass


class IncomeDeleteForm(IncomeBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'
