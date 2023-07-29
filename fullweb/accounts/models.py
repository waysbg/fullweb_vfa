from datetime import timedelta
from django.contrib.auth.models import UserManager
from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_models
from django.db.models.signals import post_save
from django.dispatch import receiver
from fullweb.accounts.validators import letters_numbers_underscore_validator, maximum_two_underscores_validator
from django.utils import timezone


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):

    username = models.CharField(
        validators=(MinLengthValidator(6),
                    letters_numbers_underscore_validator,
                    maximum_two_underscores_validator,),
        unique=True,
        null=False,
        blank=False,
        max_length=30,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    date_joined = models.DateTimeField(
        default=timezone.now,
        null=True,
        blank=True,
    )

    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    is_active = models.BooleanField(
        default=True,
        null=False,
        blank=False,
    )

    USERNAME_FIELD = 'username'

    objects = UserManager()

    class Meta:
        ordering = ('pk',)
        verbose_name_plural = 'Users'

    @property
    def year_out(self):
        if self.last_login:
            if timezone.now() - timedelta(365) > self.last_login:
                return 'Yes'
            return 'No'
        return 'No'

    @property
    def days_out(self):
        if self.last_login:
            return (timezone.now() - self.last_login).days
        return 0


class Profile(models.Model):
    avatar_photo = models.URLField(
        null=True,
        blank=True,
    )

    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, primary_key=True, related_name='profile')

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        if self.avatar_photo:
            return f"{self.user.username} - {self.avatar_photo[0:25]}..."
        else:
            return self.user.username


@receiver(post_save, sender=AppUser)
def create_empty_user_profile(sender, instance, created, **kwargs):
    if created:
        if not hasattr(instance, 'profile'):
            Profile.objects.create(user=instance)
