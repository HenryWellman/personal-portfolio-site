from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    desc = models.TextField()


    #Test for photo
class DisplayPhoto(models.Model):
    photo = models.ImageField(upload_to="gallery")
