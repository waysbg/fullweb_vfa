
from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.urls import reverse
from fullweb.bills.models import Bill
from fullweb.bills.views import ListBillsView

UserModel = get_user_model()


class BillListViewTest(TestCase):

    def test_bill_list_view_without_bills_expect_empty_list(self):

        username = 'test_user_123'
        password = 'test@123'

        user_1_data = {
            'username': username,
            'password': password,
        }

        UserModel.objects.create_user(**user_1_data)
        self.client.login(**user_1_data)

        response = self.client.get(reverse('bills list'))
        self.assertEqual(0, len(response.context['bill_list']))

    def test_bill_list_view_when_have_bills_expect_list_bills_and_total_amount(self):

        username = 'test_user_123'
        password = 'test@123'

        user_1_data = {
            'username': username,
            'password': password,
        }

        UserModel.objects.create_user(**user_1_data)
        self.client.login(**user_1_data)
        user_1 = UserModel.objects.get(username=username)

        bills_count = 5
        [Bill.objects.create(description=f'Tax {i}', amount=10, user_id=user_1.pk) for i in range(1, bills_count + 1)]

        response = self.client.get(reverse('bills list'))

        self.assertEqual(5, len(list(response.context['bill_list'])))
        self.assertEqual(50, response.context['total_amount'])

    def test_bill_list_view_when_staff_logged_in_expect_full_list_and_full_total_amount(self):

        username_1 = 'test_user_123'
        password_1 = 'test@123'

        user_1_data = {
            'username': username_1,
            'password': password_1,
        }

        UserModel.objects.create_user(**user_1_data)
        self.client.login(**user_1_data)
        user_1 = UserModel.objects.get(username=username_1)

        bills_count = 5
        [Bill.objects.create(description=f'Tax {i}', amount=10, user_id=user_1.pk) for i in range(1, bills_count + 1)]

        response = self.client.get(reverse('bills list'))

        self.assertEqual(5, len(list(response.context['bill_list'])))
        self.assertEqual(50, response.context['total_amount'])

        username_2 = 'test_staff_123'
        password_2 = 'test@123'

        user_2_staff_data = {
            'username': username_2,
            'password': password_2,
            'is_staff': True,
        }

        UserModel.objects.create_user(**user_2_staff_data)
        self.client.login(**user_2_staff_data)
        staff_2 = UserModel.objects.get(username=username_2)

        [Bill.objects.create(description=f'Tax {i}', amount=10, user_id=staff_2.pk) for i in range(1, bills_count + 1)]

        response = self.client.get(reverse('bills list'))

        self.assertEqual(10, len(list(response.context['bill_list'])))
        self.assertEqual(100, response.context['total_amount'])


    def test_bill_list_view_filter_is_used_expect_to_show_selected_list_and_correct_total_amount(self):

        username_1 = 'test_user_123'
        password_1 = 'test@123'

        user_1_data = {
            'username': username_1,
            'password': password_1,
        }

        UserModel.objects.create_user(**user_1_data)
        self.client.login(**user_1_data)
        user_1 = UserModel.objects.get(username=username_1)

        Bill.objects.create(date='2023-01-01', description='Electricity', amount=100, user_id=user_1.pk)
        Bill.objects.create(date='2023-01-02', description='Electricity', amount=200, user_id=user_1.pk)

        factory = RequestFactory()
        url = reverse('bills list')

        request = factory.get(url, data={
            'start_date_search': '2023-01-01',
            'end_date_search': '2023-01-03',
            'description_search': 'Electricity',
            'start_amount_search': '100',
            'end_amount_search': '200'
        })
        request.user = user_1

        response = ListBillsView.as_view()(request)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.context_data['start_date_search'], '2023-01-01')
        self.assertEqual(response.context_data['end_date_search'], '2023-01-03')
        self.assertEqual(response.context_data['description_search'], 'Electricity')
        self.assertEqual(response.context_data['start_amount_search'], '100')
        self.assertEqual(response.context_data['end_amount_search'], '200')

        queryset = response.context_data['object_list']
        self.assertEqual(queryset.count(), 2)
        self.assertEqual(queryset.first().description, 'Electricity')
        self.assertEqual(queryset.first().amount, 200)
        self.assertEqual(response.context_data['total_amount'], 300)




