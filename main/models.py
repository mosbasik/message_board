from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
