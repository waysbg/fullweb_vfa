from django.contrib.auth import forms as auth_forms, get_user_model
from fullweb.accounts.models import Profile
from django import forms

UserModel = get_user_model()


class SignUpForm(auth_forms.UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Insert Username',}),
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Insert Password',}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Password',})
    )

    class Meta:
        model = UserModel
        fields = ['username', 'password1', 'password2']
        field_classes = {'username': auth_forms.UsernameField,}

    # #save with empty profile
    # def save(self, commit=True):
    #     user = super().save(commit=commit)
    #     profile = Profile(
    #         user=user,
    #     )
    #     if commit:
    #         profile.save()
    #     return user

class SignInForm(auth_forms.AuthenticationForm):

    username = auth_forms.UsernameField(widget=forms.TextInput(
        attrs={'placeholder': 'Insert Username',}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Insert Password',}))


class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['avatar_photo',]

        labels = {
            'avatar_photo': 'Photo URL:'
        }

        widgets = {
            'avatar_photo': forms.URLInput(
                attrs={
                    'placeholder': 'Insert photo URL',
                },
            ),
        }

