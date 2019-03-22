from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "Placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "Placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect ('/')

def show(request, number):
    response = f'Placeholder to display blog {number}'
    return HttpResponse(response)

def edit(request, number):
    response = f'Placeholder to edit blog {number}'
    return HttpResponse(response)

def destroy(request, number):
    return redirect ('/')