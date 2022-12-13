from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class new_user(UserCreationForm):
    password2 = forms.CharField(
        label="confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username"]


def mail_check(value):
    if "gmail.com" in value:
        try:
            a = User.objects.get(email=value)
        except User.DoesNotExist:
            raise forms.ValidationError("Incorrect User or Password")
        else:
            return value


class log_in(forms.ModelForm):
    email = forms.EmailField(required=True, validators=[mail_check])
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email", "password"]
