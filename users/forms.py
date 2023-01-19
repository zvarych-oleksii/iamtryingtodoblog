from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm

from users.models import Profile


class SignUpForm(UserCreationForm):
  #  email = forms.EmailField(max_length=50, help_text="Required")
  password1 = forms.CharField(
      label="Password",
      widget=forms.PasswordInput(
          attrs={"class": "form-control form-control-lg"}),
  )
  password2 = forms.CharField(
      label="Confirm password",
      widget=forms.PasswordInput(
          attrs={"class": "form-control form-control-lg", }),
  )
  class Meta:
        model = User
        widgets = {"username":forms.TextInput(attrs={"class": "form-control form-control-lg"}),
                   "email":forms.TextInput(attrs={"class": "form-control form-control-lg"}),
                   "first_name":forms.TextInput(attrs={"class": "form-control form-control-lg margin_own"}),
                   "last_name":forms.TextInput(attrs={"class": "form-control form-control-lg"})}
        fields = {"username", "email", "first_name", "last_name", "password1", "password2"}
class ChangeUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               help_text=User.username,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', "email"]
class ProfileChangeForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    avatar = forms.ImageField(required=False,
                              widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "avatar"]
    def clean(self):
        self.instance

        """widgets = {"user_email":forms.TextInput(attrs={"class": "form-control form-control-lg"}),
                   "first_name":forms.TextInput(attrs={"class": "form-control form-control-lg"}),
                   "last_name":forms.TextInput(attrs={"class": "form-control form-control-lg"})}"""
"""class LoginForm(AuthenticationForm):
    password = forms.CharField(
      label="Confirm password",
      widget=forms.PasswordInput(
          attrs={"class": "form-control form-control-lg", }),
    )
    class Meta:
        model = User
        widgets = {"username":forms.TextInput(attrs={"class": "form-control form-control-lg"})}
        fields = {"username", "password"}
"""