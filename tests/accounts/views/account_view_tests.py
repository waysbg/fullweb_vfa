from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

UserModel = get_user_model()


class SignUpViewTests(TestCase):

    def test_create_user_with_success_login_redirect(self):

        username = "test_user_123"
        password = "test@123"

        credentials = {
            'username': username,
            'password': password
        }

        UserModel.objects.create_user(**credentials)
        logged_in = self.client.login(**credentials)

        response = self.client.post(
            reverse('sign up'),
            data=credentials,
        )

        created_user = UserModel.objects.filter(username=username).get()

        self.assertIsNotNone(created_user)
        self.assertTrue(logged_in)
        self.assertEqual(200, response.status_code)


    def test_access_profile_pages_when_anonymous_user_expect_redirect_to_login(self):

        username = 'test_user_223'
        password = 'test@123'

        user_data = {
            'username': username,
            'password': password,
        }

        UserModel.objects.create_user(**user_data)
        user_trying_to_get_access = UserModel.objects.filter(username=username).get()

        response = self.client.get(
            reverse('profile details', kwargs={'pk':user_trying_to_get_access.pk,}),
        )
        self.assertEqual(302, response.status_code)
        expected_redirect_url = f'{settings.LOGIN_URL}?next={reverse("profile details", kwargs={"pk":user_trying_to_get_access.pk,})}'
        self.assertEqual(expected_redirect_url, response.headers.get('Location'))


        response = self.client.get(
            reverse('profile edit', kwargs={'pk':user_trying_to_get_access.pk,}),
        )
        self.assertEqual(302, response.status_code)
        expected_redirect_url = f'{settings.LOGIN_URL}?next={reverse("profile edit", kwargs={"pk":user_trying_to_get_access.pk,})}'
        self.assertEqual(expected_redirect_url, response.headers.get('Location'))


        response = self.client.get(
            reverse('profile delete', kwargs={'pk':user_trying_to_get_access.pk,}),
        )
        self.assertEqual(302, response.status_code)
        expected_redirect_url = f'{settings.LOGIN_URL}?next={reverse("profile delete", kwargs={"pk":user_trying_to_get_access.pk,})}'
        self.assertEqual(expected_redirect_url, response.headers.get('Location'))


        response = self.client.get(
            reverse('password change', kwargs={'pk':user_trying_to_get_access.pk,}),
        )
        self.assertEqual(302, response.status_code)
        expected_redirect_url = f'{settings.LOGIN_URL}?next={reverse("password change", kwargs={"pk":user_trying_to_get_access.pk,})}'
        self.assertEqual(expected_redirect_url, response.headers.get('Location'))