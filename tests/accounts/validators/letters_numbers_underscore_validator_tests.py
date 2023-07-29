from unittest import TestCase
from fullweb.accounts.validators import letters_numbers_underscore_validator
from django.core.exceptions import ValidationError


class LettersNumbersUnderscoreValidatorTests(TestCase):

    def test_validator_with_correct_data_expect_correct_result(self):
        letters_numbers_underscore_validator('test_123')

    def test_validator_with_wrong_symbols_inside_expect_validation_error(self):
        with self.assertRaises(ValidationError) as error:
            letters_numbers_underscore_validator('test_123@%')
        self.assertEqual(error.exception, ValidationError('Inside username, only letters, numbers or underscores are allowed'))
