from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import User

def basepage(request):
    return render(request,'app1/registration_and_login.html')

def register(request):
    print "inside register method"
    errorz=User.objects.validation_of_registration(request.POST)
    if len(errorz) > 0:
        for error in errorz:
            messages.error(request,error)

        return redirect('/')
    else:
        personvariable = User.objects.create(
        # leftside is from models=rightside is from the forms
        name=request.POST['name'],
        email=request.POST['email'],
        Password=request.POST['password'],
        dob=request.POST['dob'],
        )
        request.session['name']=request.POST['name']
        request.session['id']=personvariable.id
        return redirect('/appointments')

def login(request):
    errorz=User.objects.validation_of_login(request.POST)
    if len(errorz):
        for error in errorz:
            messages.error(request,error)
        return redirect('/')
    else:
        loginvariable=User.objects.get(email=request.POST['email'])
        print loginvariable
        request.session['email']=loginvariable.email
        request.session['id']=loginvariable.id
        request.session['name']=loginvariable.name
        return redirect('/appointments')
