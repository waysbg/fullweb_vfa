from datetime import timedelta
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

UserModel = get_user_model()


class UserModelPropertiesTests(TestCase):

    def test_usermodel_year_out_without_last_login_data_expect_result_NO(self):
        user = UserModel(
            username="waysbg",
            password="test@123"
        )

        user.full_clean()
        user.save()

        self.assertEqual(user.year_out, 'No')

    def test_usermodel_year_out_with_last_login_today_expect_result_NO(self):
        user = UserModel(
            username="waysbg",
            password="test@123",
            last_login=timezone.now(),
        )

        user.full_clean()
        user.save()

        self.assertEqual(user.year_out, 'No')

    def test_usermodel_year_out_with_last_login_before_364_days_expect_result_NO(self):
        user = UserModel(
            username="waysbg",
            password="test@123",
            last_login=timezone.now() - timedelta(364),
        )

        user.full_clean()
        user.save()

        self.assertEqual(user.year_out, 'No')

    def test_usermodel_year_out_with_last_login_exactly_365_days_ago_expect_result_Yes(self):
        user = UserModel(
            username="waysbg",
            password="test@123",
            last_login=timezone.now() - timedelta(365),
        )

        user.full_clean()
        user.save()

        self.assertEqual(user.year_out, 'Yes')

    def test_usermodel_year_out_with_last_login_more_than_365_days_expect_result_Yes(self):
        user = UserModel(
            username="waysbg",
            password="test@123",
            last_login=timezone.now() - timedelta(366),
        )

        user.full_clean()
        user.save()

        self.assertEqual(user.year_out, 'Yes')

    def test_usermodel_days_out_without_last_login_data_expect_result_0(self):
        user = UserModel(
            username="waysbg",
            password="test@123"
        )

        user.full_clean()
        user.save()

        self.assertEqual(user.days_out, 0)

    def test_usermodel_days_out_with_last_login_today_expect_result_0(self):
        user = UserModel(
            username="waysbg",
            password="test@123",
            last_login=timezone.now(),
        )

        user.full_clean()
        user.save()

        self.assertEqual(user.days_out, 0)

    def test_usermodel_days_out_with_last_login_before_364_days_expect_result_364(self):
        user = UserModel(
            username="waysbg",
            password="test@123",
            last_login=timezone.now() - timedelta(364),
        )

        user.full_clean()
        user.save()

        self.assertEqual(user.days_out, 364)
