from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=255)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    def __str__(self):
        return str(self.id)
    
class Device(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    availability=models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField(blank=True,null=True)
    return_date = models.DateTimeField(blank=True,null=True)
    checkout_condition = models.TextField(blank=True)
    return_condition = models.TextField(blank=True,null=True)

