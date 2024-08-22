from django.db import models

# Create your models
class Student(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    age=models.IntegerField(null=True)
    corecourse=models.CharField(max_length=10)
    address=models.CharField(max_length=20)
    dateofjoin=models.DateField(null=True)
    images=models.ImageField(upload_to='image/',null=True)

