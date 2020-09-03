from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Hospitals(models.Model):
    code = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    h_type = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.code + " : " + self.label

class Service(models.Model):
    CATEGORY = (
        ('call','call'),
        ('line','line'),
        ('facebook','facebook'),
        ('email','email'),
    )
    name = models.CharField(max_length=255,null=True, choices=CATEGORY)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Case(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project, null=True,on_delete= models.SET_NULL)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resolution = models.TextField()
    service = models.ForeignKey(Service, null=True, on_delete= models.SET_NULL)
    hospitals = models.ForeignKey(Hospitals, null=True, on_delete= models.SET_NULL)
    date_entered = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField()

    def __str__(self):
        return str(self.id) + ' : '+ self.name