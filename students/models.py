from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    qualification = models.CharField(max_length=200)
    percentage = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
