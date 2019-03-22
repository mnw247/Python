from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.db import IntegrityError
from django import forms
import bcrypt
from .models import *

def index(request):
    return render(request,'trip/index.html')

def dashboard(request):
    if "id" in request.session:
        content = {
            "trips" : Trip.objects.filter(trip_members = request.session['id']), 
            "alltrips" : Trip.objects.exclude(trip_members=request.session['id'])
            }
        return render(request,'trip/dashboard.html', content)
    else:
        return redirect('/')

def login(request):
    try:
        user = User.objects.get(email=request.POST['login_email'])
        if bcrypt.checkpw(request.POST['login_password'].encode(), user.password.encode()):
            request.session['first_name'] = user.first_name
            request.session['id'] = user.id
            return redirect('/dashboard')
    except User.DoesNotExist:
        pass
    messages.error(request, 'Login unsuccessful. Plase check email and passowrd, and try again.', extra_tags='login')
    return redirect('/')

def register(request):
    errors = User.objects.validator(request.POST)
    pwHash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')
    else:
        try:
            user = User.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'],email = request.POST['email'],password = pwHash)
        except IntegrityError:
            messages.error(request, 'this email already exists', extra_tags='email')
            return redirect('/')
    request.session['first_name'] = request.POST['first_name']
    request.session['id'] = user.id
    return redirect('/dashboard')

def logout(request)    :
    request.session.flush()
    return redirect('/')

def addtrip(request):
    if "id" in request.session:
        return render(request,'trip/addtrip.html')
    return redirect("/")

def tripadded(request):
    errors = Trip.objects.tripValidator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/addtrip')
    else:
        Trip.objects.create(
            destination=request.POST['destination'],
            description=request.POST['description'],
            sdate=request.POST['sdate'],
            edate=request.POST['edate'], 
            creator = User.objects.get(id = request.session['id'])
        )
    UID = User.objects.get(id=request.session['id'])
    TID = Trip.objects.last()
    UID.joined_trips.add(TID)
    return render(request,'trip/addtrip.html')

def view(request,id):
    trip = Trip.objects.get(id=id)
    content = {
        "trip":trip,
        "joinedusers":trip.trip_members.all()
    }
    #"joinedusers":User.objects.filter(joined_trips=Trip.objects.get(id=id))
    return render(request,'trip/view.html', content)

def join(request,id):
    UID = User.objects.get(id=request.session['id'])
    TID = Trip.objects.get(id=id)
    UID.joined_trips.add(TID)
    return redirect('/dashboard')

def cancel(request,id):
    UID = User.objects.get(id=request.session['id'])
    TID = Trip.objects.get(id=id)
    UID.joined_trips.remove(TID)
    return redirect('/dashboard')

def delete(request,id):
    TID = Trip.objects.get(id=id)
    TID.delete()
    return redirect('/dashboard')