from django import forms
from fullweb.other.models import Other


class OtherBaseForm(forms.ModelForm):

    class Meta:
        model = Other
        fields = ['date', 'description', 'amount']

        labels = {
            'date': 'Other date'
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


class OtherCreateForm(OtherBaseForm):
    pass


class OtherEditForm(OtherBaseForm):
    pass


class OtherDeleteForm(OtherBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'
