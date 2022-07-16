from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class": "form-control my-3", "placeholder": "Enter email"}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class": "form-control my-3", "placeholder": "Enter password"}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class": "form-control my-3", "placeholder": "Repeat password"}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter username"}),
        }
    
    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user