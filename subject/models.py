from django.db import models

# Create your models here.


class Subject(models.Model):
    code = models.CharField(max_length=8)
    name = models.CharField(max_length=50)
    unit = models.PositiveSmallIntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add=True)
    