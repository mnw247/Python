from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.db import IntegrityError
from django import forms
import bcrypt
from .models import *

def index(request):
    return render(request,'jobs/index.html')

def dashboard(request):
    if "id" in request.session:
        content = {
            "jobs" : Job.objects.filter(jobsadded__id = request.session['id']), 
            "alljobs" : Job.objects.exclude(jobsadded__id = request.session['id'])
            }
        return render(request,'jobs/dashboard.html', content)
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

def addjob(request):
    if "id" in request.session:
        return render(request,'jobs/addjob.html')
    return redirect("/")

def jobadd(request):
    errors = Job.objects.jobValidator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/addjob')
    else:
        Job.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            location=request.POST['location'],
            creator = User.objects.get(id = request.session['id'])
        )
    return redirect('/dashboard')

def edit(request, id):
    job = Job.objects.get(id=id)
    return render(request, 'jobs/edit.html', {'job':job})

def editsubmit(request, id):
    errors = Job.objects.jobValidator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect(f'/edit/{id}')
    else:
        job = Job.objects.get(id=id)
        job.title = request.POST['title']
        job.description = request.POST['description']
        job.location = request.POST['location']
        job.save()
    return redirect('/dashboard')

def view(request,id):
    job = Job.objects.get(id=id)
    content = {
        "job":job,
        # "joinedusers":job.job_members.all()
    }
    #"joinedusers":User.objects.filter(joined_jobs=Job.objects.get(id=id))
    return render(request,'jobs/view.html', content)

def join(request,id):
    UID = User.objects.get(id=request.session['id'])
    TID = Job.objects.get(id=id)
    UID.joined_jobs.add(TID)
    return redirect('/dashboard')

def delete(request,id):
    TID = Job.objects.get(id=id)
    TID.delete()
    return redirect('/dashboard')

# def cancel(request,id):
#     UID = User.objects.get(id=request.session['id'])
#     TID = Job.objects.get(id=id)
#     UID.joined_jobs.remove(TID)
#     return redirect('/dashboard')