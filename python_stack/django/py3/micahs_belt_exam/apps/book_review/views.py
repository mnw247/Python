from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt
from datetime import datetime
from django.contrib.auth import logout

def index(request):
    return render(request,'index.html')

def register(request):
    errors = User.objects.regValidator(request.POST)

    if len(errors):
        for key, value in errors.items(): messages.error(request, value)
        return redirect('/')
    else:
        user=User.objects.create(first_name = request.POST['first_name'], alias = request.POST['alias'], email = request.POST['email'], password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
        request.session['id'] = user.id	
        return redirect('/books')

def login(request):
    err = User.objects.loginValidator(request.POST)
    if err:
        for key,value in err.items():
            print('key:', key, 'value', value)
            messages.error(request, value)
        return redirect('/')
    request.session['id'] = User.objects.get(email = request.POST['email_login']).id
    return redirect('/books')
#
def books(request):
    content = {
        'reviews': Review.objects.all().order_by('-created_at')[:3],
        'reviewed_books' : Book.objects.all()
    }
    x='1'
    for i in range(3):
        for y in range(content['reviews'][i].rating):
            x = x + '1'
        print(x)
    content['rating'] = x
    return render(request,'books.html', content)

def booksAdd(request):
    content = {
        'books': Book.objects.all()
    }
    return render(request,'login_registration/bookAdd.html', content)

def addBooks(request):
    if len(request.POST['newauthor']) > 1:
        book = Book.objects.create(name=request.POST['title'],author=request.POST['newauthor'])
        user = User.objects.get(id = request.session['id'])
        Reviews.objects.create(user=user,book = book,review = request.POST['review'],rating = request.POST['rating'])
        book.save()
    else:
        book = Book.objects.create(name=request.POST['title'],author=request.POST['author'])
        user = User.objects.get(id = request.session['id'])
        Reviews.objects.create(user=user,book = book,review = request.POST['review'],rating = request.POST['rating'])
        book.save()
    return redirect(f'/book/{book.id}/')

def addReview(request,id):
    book = Book.objects.get(id=id)
    user = User.objects.get(id = request.session['id'])
    Reviews.objects.create(user=user,book = book,review = request.POST['review'],rating = request.POST['rating'])
    return redirect(f'/book/{book.id}/')

def book(request,id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        messages.error(request,'Book does not exists')
    content = {
        'reviews': book.books_reviewed.all(),
        'book': book
    }
    return render(request,'login_registration/book.html',content)   

def users(request,id):
    user = User.objects.get(id=id)
    content = {
        'user': user,
        'books': User.objects.raw(f'select distinct login_registration_book.id,book_id,name from login_registration_reviews join login_registration_book on login_registration_reviews.book_id = login_registration_book.id  where user_id = {id}'),
        'cnt' : user.reviewed_books.count()
    }
    return render(request,'login_registration/users.html',content)


def destroy(request):
    hello = "world"
    return hello

def logout_view(request):
    logout(request)
    return redirect('/')



