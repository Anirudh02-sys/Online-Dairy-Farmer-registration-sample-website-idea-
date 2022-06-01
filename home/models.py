from django.db import models
from sqlalchemy import true


class Member(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phno = models.IntegerField()
    password = models.CharField(max_length=50)

    class Meta:
        app_label = 'home'
        abstract = true

    def __str__(self):
        pass


class Farmer(Member):
    cert1 = models.BooleanField(default=False)
    cert2 = models.BooleanField(default=False)
    cert3 = models.BooleanField(default=False)

    def __str__(self):
        type = 'Farmer'
        return self.fname+' '+self.lname+'('+type+')'


class Consumer(Member):
    def __str__(self):
        type = 'Consumer'
        return self.fname+' '+self.lname+'('+type+')'


class Company(Member):
    auth = models.BooleanField()

    def __str__(self):
        utype = 'Company'
        return self.fname+' '+self.lname+'(' + utype + ')'
