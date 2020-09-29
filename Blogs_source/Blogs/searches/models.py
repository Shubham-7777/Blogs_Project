from django.db import models
from django.conf import settings

USER = settings.AUTH_USER_MODEL
# Create your models here.


class SearchModel(models.Model):
    user = models.ForeignKey(USER, null=True, on_delete=models.SET_NULL)
    query = models.CharField(max_length=220)
    timestamp = models.DateTimeField(auto_now_add=True)
