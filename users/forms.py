from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile
from django.utils.translation import gettext_lazy as _


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': _('Username (Please make your username recognisable for your buddy.)'),
        }



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
            'username': _('Username (Please make your username recognisable for your buddy.)'),
        }



class ProfileUpdateForm(forms.ModelForm):
    buddy = forms.ModelChoiceField(queryset=User.objects.exclude(username='admin').order_by('username'))
    class Meta:
        model = Profile
        fields = ['goal', 'buddy']
