from unittest import TestCase
from fullweb.accounts.validators import maximum_two_underscores_validator
from django.core.exceptions import ValidationError


class MaximumTwoUnderscoresValidatorTests(TestCase):

    def test_validator_with_correct_data_expect_correct_result(self):
        maximum_two_underscores_validator('test__123')

    def test_validator_without_any_underscores_expect_correct_result(self):
        maximum_two_underscores_validator('test123')

    def test_validator_with_more_than_two_underscores_expect_validation_error(self):
        with self.assertRaises(ValidationError) as error:
            maximum_two_underscores_validator('test___123')
        self.assertEqual(error.exception, ValidationError('Maximum two underscores are allowed inside username'))
