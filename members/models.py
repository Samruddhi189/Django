from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=225)
    lastname = models.CharField(max_length=225)
    mobile_no = models.IntegerField()
    joined_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}    {self.mobile_no}   {self.joined_date}"
    

class Teacher(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    age = models.IntegerField()
    mobile_no = models.IntegerField()
    created_by = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.age} {self.mobile_no}"
