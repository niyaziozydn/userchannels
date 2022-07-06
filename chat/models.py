from django.db import models
from django.contrib.auth.models import User

class CheckUser(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    is_online = models.BooleanField(default=False)
