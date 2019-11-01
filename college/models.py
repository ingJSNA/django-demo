from django.db import models


# Create your models here.

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)


class Professor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)


class Score(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=4, decimal_places=2)