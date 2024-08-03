from django.db import models
from django.contrib.auth.models import AbstractUser
from program.models import Program

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    student_code = models.CharField(max_length=20, unique=True)
    program = models.ForeignKey(Program, on_delete=models.PROTECT)
    gpa = models.FloatField(default=0.0)
    year = models.PositiveSmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    