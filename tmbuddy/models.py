from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


ROLE_CHOICES = [
    ('Toastmaster', 'Toastmaster'),
    ('Timer', 'Timer'),
    ('Word of the day/Grammarian', 'Word of the day/Grammarian'),
    ('Toast of the day', 'Toast of the day'),
    ('Speaker - Prepared speech', 'Speaker - Prepared speech'),
    ('Evaluator - Prepared speech', 'Evaluator - Prepared speech'),
    ('Table topics master', 'Table topics master'),
    ('Speaker - Table topics', 'Speaker - Table topics'),
    ('Evaluator - Table topics', 'Evaluator - Table topics'),
    ('Hark and fine', 'Hark and fine'),
    ('Ah counter', 'Ah counter'),
    ('General Evaluator', 'General Evaluator'),
]

SCORE_CHOICES = [
    ('1-Developing', '1-Developing'),
    ('2-Emerging', '2-Emerging'),
    ('3-Accomplished', '3-Accomplished'),
    ('4-Excel', '4-Excel'),
    ('5-Exemplary', '5-Exemplary'),
]


class SelfReflection(models.Model):
    content = models.TextField()
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    score = models.CharField(max_length=50, choices=SCORE_CHOICES)
    meeting_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-meeting_date']

    def __str__(self):
        return "%s's meeting reflection - %s" % (self.meeting_date, self.user)

    def get_absolute_url(self):
        return reverse('user-reflection', kwargs={'username': self.user.username})


class BuddyFeedback(models.Model):
    content = models.TextField()
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    score = models.CharField(max_length=50, choices=SCORE_CHOICES)
    meeting_date = models.DateField()
    from_user = models.ForeignKey(User, related_name='given_feedback', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='received_feedback', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-meeting_date']

    def __str__(self):
        return "%s's meeting buddy feedback - from %s, to %s" % (self.meeting_date, self.from_user, self.to_user)

    def get_absolute_url(self):
        return reverse('user-given-feedback', kwargs={'username': self.from_user.username})
