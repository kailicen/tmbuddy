from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    goal = models.CharField(max_length=200, null=True)
    buddy = models.ForeignKey(User, null=True, related_name='buddy', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'