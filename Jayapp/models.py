from django.db import models

class Students(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    emailaddress = models.EmailField(max_length=30)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    class Meta:
        db_table = 'wanafunzi'

class Teachers(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    emailaddress = models.EmailField()
    def __str__(self):
        return self.FirstName

class Parents(models.Model):
    Name = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=20)
    Residence = models.CharField(max_length=20)
    age = models.IntegerField()
    def __str__(self):
        return self.Name

class host(models.Model):
    title = models.CharField(max_length=20)
    Author = models.CharField(max_length=20)
    CreationDate = models.DateField()
    def __str__(self):
        return self.title
