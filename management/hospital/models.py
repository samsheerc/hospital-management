from django.db import models 
from django.contrib.auth.models import User 
from django.db import models
from django.shortcuts import render







class  Department(models.Model):
    dep_name= models.TextField(max_length=50)
    dep_desc=models.TextField(max_length=200)
    
    def __str__(self):
        return self.dep_name
    

class Doctor(models.Model):
    doc_name=models.CharField(max_length=100)
    doc_dep=models.ForeignKey(Department,on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to='doctores/')

    def __str__(self):
        return self.doc_name
    
    def appointments(self):
        return Appointment.objects.filter(doctor=self)

class Booking(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=40) 
    phone=models.CharField(max_length=12) 
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    booked=models.DateField()
    time=models.TimeField()
    desc=models.TextField(max_length=500)
    
   
    
    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    # Add other relevant fields

    def __str__(self):
        return f"{self.patient_name}'s Appointment with Dr. {self.doctor}"   
    

class UserProfile(models.Model):
     name = models.CharField(max_length=100,default='Anonymus')
  



class Contact(models.Model):
    name= models.CharField(max_length=100,default="null")
    email= models.CharField(max_length=50)
    subject= models.CharField(max_length=50)
    message=models.TextField(max_length=50)
     
    def __str__(self):
        return self.name
    
class Feedback(models.Model):
    name=models.CharField(max_length=50)  
    email=models.CharField(max_length=50)
    message=models.TextField(max_length=100)