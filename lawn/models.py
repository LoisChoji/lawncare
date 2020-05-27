from django.db import models

# Create your models here.
class Lawning(models.Model):
    instructor_name = models.CharField(max_length = 100)
    part_name = models.CharField(max_length = 100)
    #partname is participants name
    images = models.ImageField(upload_to = "pics")
    category = models.TextField()
    started_from =models.DateField('started_from')

    #nb:after creating your models go to pgadmin
    #create a database with your project name them makemigrations