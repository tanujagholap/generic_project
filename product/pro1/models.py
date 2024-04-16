from django.db import models


class Student(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=20)
    marks = models.IntegerField()
    standard = models.IntegerField()
