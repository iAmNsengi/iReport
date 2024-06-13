from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=10,default='0')
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
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True,blank=True)
    cat1 = models.FloatField(default=0.0)
    cat2 =models.FloatField(default=0.0)
    fat = models.FloatField(default=0.0)
    total = models.FloatField(default=0.0)

    def save(self, *args, **kwargs):
        self.total = self.cat1 + self.cat2 + self.fat
        super(Data, self).save(*args, **kwargs)
