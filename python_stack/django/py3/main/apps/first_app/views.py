from django.shortcuts import render, HttpResponse, redirect

def index(req):
    response = "Hello, I am your first request!"
    return HttpResponse(response)
