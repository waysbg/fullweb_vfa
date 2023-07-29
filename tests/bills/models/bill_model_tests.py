from django.contrib.auth import get_user_model
from django.test import TestCase

from fullweb.bills.models import Bill

UserModel = get_user_model()


class BillModelTests(TestCase):

    def test_bill_model_with_bill_and_user_str_expect_correct(self):

        username = 'test_user_123'
        password = 'test@123'

        user_1_data = {
            'username': username,
            'password': password,
        }

        UserModel.objects.create_user(**user_1_data)
        self.client.login(**user_1_data)
        user_1 = UserModel.objects.get(username=username)


        user_1_bill_1_data = {
            'description': 'Electricity',
            'amount': 10,
            'user': user_1
        }


        user_1_bill_1 = Bill.objects.create(**user_1_bill_1_data)
        self.assertIsNotNone(user_1_bill_1)

        str_expected_result = f"Bill - {username} - Electricity - 10.00 $"

        self.assertEqual(str(user_1_bill_1), str_expected_result)

