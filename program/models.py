from django.db import models
from faculty.models import Major
# Create your models here.


class Program(models.Model):
    major = models.ForeignKey(Major, on_delete=models.PROTECT)
    detail = models.JSONField()
    version = models.PositiveIntegerField(default=1)
