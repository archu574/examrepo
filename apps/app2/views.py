# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from datetime import date
from django.utils.timezone import datetime
from ..app1.models import User
from ..app2.models import Appointment
from django.shortcuts import render,redirect
from django import forms



# Create your views here.
def contextfunc(request):


    today = datetime.today()

    # today = datetime.date()
    myapptstoday=Appointment.objects.filter(userappointments_id=request.session['id'])

    myapptstoday2=Appointment.objects.filter(datee__year=today.year, datee__month=today.month, datee__day=today.day)

    s1=set(myapptstoday)
    s2=set(myapptstoday2)

    s2=s2-s1

    otherappts=Appointment.objects.filter(userappointments_id=request.session['id'])
    otherappts2=Appointment.objects.exclude(datee__year=today.year, datee__month=today.month, datee__day=today.day)
    y1=set(otherappts)
    y2=set(otherappts2)
    y1=y1-y2

    context={
        'myappttoday':s2,
        'otherappt':y1
    }
    return render(request,'app2/dashboard.html',context)

def logout(request):
    return redirect('/')
def addappointment(request):
    print "adding appt views func"
    id=request.session['id']
    entry=Appointment.objects.addappt(id,request.POST)
    return redirect('/appointments')

def update(request,appointment_id):
    apptt=Appointment.objects.get(id=appointment_id)
    context={
        'a':apptt
    }
    return render(request,'app2/editingpage.html',context)

def editing(request,appointment_id):
    editingvariable=Appointment.objects.get(id=appointment_id)
    editingvariable.task=request.POST['taskdata']
    editingvariable.status=request.POST['status_choices']
    editingvariable.datee=request.POST['datedata']
    editingvariable.timee=request.POST['timedata']
    editingvariable.save()
    return redirect('/appointments')

def deleting(request,appointment_id):
    Appointment.objects.get(id=appointment_id).delete()
    return redirect('/appointments')
def dashboard(request):
    return redirect('/appointments')
