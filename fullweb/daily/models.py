from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.utils import timezone

UserModel = get_user_model()


class Daily(models.Model):

    date = models.DateField(
        default=timezone.now,
        max_length=20,
        null=False,
        blank=False,
    )

    description = models.CharField(
        validators=(MinLengthValidator(1),),
        max_length=100,
        null=False,
        blank=False,
    )

    amount = models.FloatField(
        null=False,
        blank=False,
        validators=(MinValueValidator(0.01),),
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('-date','-pk')
        verbose_name_plural = 'Daily'

    def __str__(self):
        return f'{self.__class__.__name__} - {self.user} - {self.description} - {self.amount:.2f} $'
