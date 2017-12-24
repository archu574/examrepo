# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..app1.models import User
from django.db import models

# Create your models here.
class AppointmentManager(models.Manager):

    def addappt(self,id,data):
        print "adding an appt"
        user=User.objects.get(id=id)
        appointments=self.create(datee=data['datedata'],timee=data['timedata'],task=data['taskdata'],userappointments=user)
        # appointments.userappointments.add(user)
        appointments.save()
        return appointments



class Appointment(models.Model):
    datee=models.DateField(auto_now=True)
    timee=models.TimeField(auto_now=True)
    task=models.TextField(max_length=5000)
    pending='p'
    done='d'
    missed='m'
    status_choices = (
        (pending, 'pending'),
        (done, 'done'),
        (missed, 'missed'),
    )
    status=models.CharField(max_length=6, choices=status_choices, default='Pending')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    userappointments = models.ForeignKey(User, related_name="relation")
    objects=AppointmentManager()
    def was_published_today(self):
        return self.created_at.date() == datetime.today().date()
