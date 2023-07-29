from django import forms
from fullweb.daily.models import Daily


class DailyBaseForm(forms.ModelForm):

    class Meta:
        model = Daily
        fields = ['date', 'description', 'amount']

        labels = {
            'date': 'Daily date'
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


class DailyCreateForm(DailyBaseForm):
    pass


class DailyEditForm(DailyBaseForm):
    pass


class DailyDeleteForm(DailyBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'
