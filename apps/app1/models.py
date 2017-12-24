from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def validation_of_registration(self,data):
        errors=[]
        if len(data['name'])<3:
            errors.append("name needs to be a minimum of 3 charachters")
        if len(User.objects.filter(email=data['email'])) > 0:
            errors.append("email already in use")
        if len(data['password'])<8:
            errors.append("password needs to be atleast a minimum of 8 charachters long")
        if not data['confirm_password'] or data['confirm_password'] != data['password']:
            errors.append("Passwords do not match please enter same password")
        return errors

    def validation_of_login(self,data):
        errors=[]

        useremail_for_validation=User.objects.filter(email=data['email'])
        if len(useremail_for_validation) < 1 :
            errors.append("email is not in our records")

        else:
            print useremail_for_validation
            print useremail_for_validation[0]
            if data['password'] != useremail_for_validation[0].Password :
                errors.append("password does not exist in our records")
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    Password=models.CharField(max_length=255)
    dob=models.DateField(auto_now=False, auto_now_add=False,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
        return self.email
