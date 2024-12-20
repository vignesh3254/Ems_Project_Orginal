from django.db import models

# Create your models here.
class Data(models.Model):
    emp_id=models.IntegerField()
    emp_name=models.CharField(max_length=100)
    emp_mail=models.EmailField(max_length=30)
    emp_city=models.CharField(max_length=10)
    
    def __str__(self):
        return self.emp_name