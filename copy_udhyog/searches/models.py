from django.db import models
from django.conf import settings

# Create your models here.


class SearchQuery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             blank=True, null=True, on_delete=models.SET_NULL)
    query = query = models.CharField(max_length=220)
    date = models.DateField(auto_now_add=True)
