from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    Roll_no = models.IntegerField()
    class_no = models.IntegerField()
    Address = models.CharField(max_length=70)
    
    def __str__(self):
        return str(self.id)

