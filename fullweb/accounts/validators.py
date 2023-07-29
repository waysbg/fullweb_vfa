from django.core.exceptions import ValidationError


def letters_numbers_underscore_validator(value:str):
    for char in value:
        if not char.isalnum() and char != '_':
            raise ValidationError('Inside username, only letters, numbers or underscores are allowed')


def maximum_two_underscores_validator(value:str):
    if value.count('_') > 2:
        raise ValidationError('Maximum two underscores are allowed inside username')
