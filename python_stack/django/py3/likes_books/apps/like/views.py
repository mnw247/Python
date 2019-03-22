from django.shortcuts import render

def index(request):
    context = {"users": User.objects.all()}
    return render(request, "books/index.html", context)
