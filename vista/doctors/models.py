from django.db import models

# Create your models here.


class Doctor(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=15, null=True , blank=True)
    mail = models.EmailField(max_length=200 , unique=True)
    password = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=200,null=True,blank=True)
    photo = models.FileField(null=True , blank=True , upload_to='photos')
    major = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=5 , decimal_places=2)
    def __str__(self):
        return self.name

class Experience(models.Model):
    name_of_hospital = models.CharField(max_length=50)
    year_of_experience = models.DecimalField(max_digits=3,decimal_places=1)
    Doctor = models.ForeignKey(Doctor , on_delete=models.CASCADE , related_name='experiences')

    def __str__(self):
        return self.name_of_hospital



class Client(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200 , unique=True)
    password = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.CharField(max_length=12 , null=True , blank=True)
    address = models.CharField(max_length=200 , null=True , blank=True)
    def __str__(self):
        return self.name

class Booking (models.Model):
    name = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    Doctor = models.ForeignKey(Doctor , on_delete= models.CASCADE , related_name='books')

    def __str__(self):
        return self.name