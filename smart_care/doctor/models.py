from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient
# Create your models here.
class Specialization(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length = 50)
    
    def __str__(self):
        return self.name
class Designation(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length = 50)

    def __str__(self):
        return self.name
class AvailableTime(models.Model):
    name = models.CharField(max_length=150)


    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='doctor/images/')
    designation = models.ManyToManyField(Designation)
    specialization = models.ManyToManyField(Specialization)
    available_time = models.ManyToManyField(AvailableTime)

    fee = models.IntegerField()
    meet_link = models.CharField(max_length = 100)


    def __str__(self):
        return f"{self.user.first_name } {self.user.last_name}"

START_CHOICES = [
    ('★','★'),
    ('★★','★★'),
    ('★★★','★★★'),
    ('★★★★','★★★★'),
    ('★★★★★','★★★★★'),
]
class Review(models.Model):
    reviewer = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    reivew = models.TextField()
    create_on = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(choices = START_CHOICES ,max_length=50)

    def __str__(self):
        return f"Doctor {self.doctor.user.first_name} Reviwed By {self.reviewer.user.first_name} Patient"
    