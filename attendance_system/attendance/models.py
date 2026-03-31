from django.db import models

# Create your models here.
class Student(models.Model): 
    name = models.CharField(max_length =100)
    student_id = models.CharField(max_length =20)
    is_present = models.BooleanField(default=False)
    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.date}"
