from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import SelfReflection, BuddyFeedback


class DateInput(forms.DateInput):
    input_type = 'date'


class SelfReflectionForm(ModelForm):

    class Meta:
        model = SelfReflection
        fields = ['meeting_date', 'role', 'score', 'content']
        widgets = {
            'meeting_date': DateInput(),
        }
        labels = {
            'content': _('Comment'),
        }


class BuddyFeedbackForm(ModelForm):
    
    class Meta:
        model = BuddyFeedback
        fields = ['meeting_date', 'role', 'score', 'content']
        widgets = {
            'meeting_date': DateInput(),
        }
        labels = {
            'content': _('Comment'),
        }