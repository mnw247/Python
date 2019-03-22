from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from .models import *

def index(request):
    return render(request,'quotes/index.html')

def login(request):
    try:
        user = User.objects.get(email=request.POST['login_email'])
        if bcrypt.checkpw(request.POST['login_password'].encode(), user.password.encode()):
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

def dashboard(request):
    if "id" in request.session:
        content = {
            'quotes':Quote.objects.all(),
            'user' : User.objects.get(id = request.session['id'])
        }
        return render(request,'quotes/dashboard.html',content)
    else:
        return redirect('/')

def addquote(request):
    Quote.objects.create(
        author=request.POST['author'],
        message=request.POST['quote'],
        created_by = User.objects.get(id = request.session['id'])
        )
    return redirect('/dashboard')

def accountupdate(request, id):
    user = User.objects.get(id=id)
    return render(request, 'quotes/edit.html', {'user':user})

def submitupdate(request, id):
    errors = User.objects.editValidator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect(f'/myaccount/{id}')
    else:
        user = User.objects.get(id=id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
    return redirect('/dashboard')

def userquotes(request, id):
    if "id" in request.session:
        content = {
            'quotes':User.objects.get(id=id).quote_added.all(), 'user':User.objects.get(id=id)
        }#or'quotes':Quote.objects.filter(created_by=id)
    return render(request, 'quotes/view.html',content)

def likedquotes(request, id):
    Like.objects.create(
        user_id=request.session['id'],
        quote_id=id
    )
    return render('/dashboard',content)

def delete(request,id):
    Quote.objects.get(id=id).delete()
    return redirect('/dashboard')

