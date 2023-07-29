from django.test import TestCase

from fullweb.bills.forms import BillDeleteForm


class BillDeleteFormTests(TestCase):

    def test_bill_delete_form_disabled_fields_expect_all_to_be_disabled(self):
        form = BillDeleteForm()

        disabled_fields = {
            name: field.widget.attrs['disabled']
            for name, field in form.fields.items()
        }

        self.assertEqual(
            'disabled',
            disabled_fields['date'],
        )

        self.assertEqual(
            'disabled',
            disabled_fields['description'],
        )

        self.assertEqual(
            'disabled',
            disabled_fields['amount'],
        )
