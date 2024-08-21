from django.db import models

# Create your models here.
class student(models.Model):
    Name=models.CharField(max_length=150)
    Email=models.CharField(max_length=150)
    Password=models.CharField(max_length=150)
    Address=models.TextField()
    Number=models.IntegerField()
    Course=models.CharField(max_length=150)
    stdimage=models.ImageField(upload_to="static/students/")
    def __str__(self):
        return self.Name
class user(models.Model):
    C_Name=models.CharField(max_length=150)
    Email=models.CharField(max_length=150)
    Password=models.CharField(max_length=150)
    Course=models.CharField(max_length=150)
    Message=models.TextField()
    def __str__(self):
        return self.C_Name