from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    current_class = models.ForeignKey('TheClass',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.first_name + " " + self.last_name


class TheClass(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    courses = models.ManyToManyField('Course')

    def __str__(self):
        return self.name + "  - " + self.code

class Course(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10)                               

    def __self__(self):
        return self.title


class Data(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    cat1 = models.FloatField()
    cat2 =models.FloatField()
    fat = models.FloatField()
    total = models.FloatField()