from django.db import models
from authen.models import User
# Create your models here.


class StudentTerm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gps = models.FloatField(default=0.0)
    subjects = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    