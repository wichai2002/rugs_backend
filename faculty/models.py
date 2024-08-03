from django.db import models
from subject.models import Subject

# Create your models here.


class Faculty(models.Model):
    name = models.CharField(max_length=200, unique=True)

class Major(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT)
    name = models.CharField(max_length=200, unique=True)
    subjects = models.ManyToManyField(Subject)
    
