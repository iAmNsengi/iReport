from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    current_class = models.ManyToManyField('TheClass')
    dob = models.CharField(max_length=20)
    

    def __str__(self):
        return self.first_name + " " + self.last_name


class TheClass(models.Model):
    name = models.CharField(max_length=10)
    code = models.CharField(max_length=5)
    courses = models.ManyToManyField('Course')

    def __str__(self):
        return self.name + "  - " + self.code

class Course(models.Model):
    title = models.CharField(max_length=10)
    code = models.CharField(max_length=5)

