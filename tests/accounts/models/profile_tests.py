from datetime import timedelta
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from fullweb.accounts.models import Profile
from django.utils import timezone

UserModel = get_user_model()


class ProfileTests(TestCase):

    def test_creation_of_empty_profile_when_user_is_created_expected_creation_of_empty_profile(self):
        user = UserModel(
            username="waysbg",
            password="test@123"
        )

        user.full_clean()
        user.save()

        profile = Profile.objects.get(user=user.pk)

        self.assertIsNotNone(profile.pk)


    def test_that_profiles_count_equal_users_count_expect_equal_counts(self):
        user_1 = UserModel(
                username=f"waysbg_1",
                password="test@123"
            )

        user_2 = UserModel(
            username="waysbg_2",
            password="test@123"
        )

        user_3 = UserModel(
            username="waysbg_3",
            password="test@123"
        )

        user_1.full_clean()
        user_1.save()
        user_2.full_clean()
        user_2.save()
        user_3.full_clean()
        user_3.save()

        profiles_count = Profile.objects.all().count()
        users_count = UserModel.objects.all().count()

        self.assertEqual(profiles_count, users_count)

    def test_profile_str_with_available_photo_expect_user_name_and_first_25_letters_from_photo_address(self):

        user_1 = UserModel(
                username=f"waysbg_1",
                password="test@123"
            )

        user_1.full_clean()
        user_1.save()

        profile_1 = Profile.objects.get(user=user_1.pk)
        profile_1.avatar_photo="https://images.pexels.com/photos/3113766/pexels-photo-3113766.jpeg"

        expected_result = 'waysbg_1 - https://images.pexels.com...'

        self.assertEqual(expected_result, str(profile_1))

    def test_profile_str_without_photo_expect_user_name(self):

        user_1 = UserModel(
                username=f"waysbg_1",
                password="test@123"
            )

        user_1.full_clean()
        user_1.save()

        profile_1 = Profile.objects.get(user=user_1.pk)

        expected_result = 'waysbg_1'

        self.assertEqual(expected_result, str(profile_1))
