from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if "attempts" in request.session:
        request.session['attempts'] += 1
    else:
        request.session["attempts"] = 0
    content = {"unique_id" : get_random_string(length=14) }
    return render(request, "generator/index.html", content)

def reset(request):
    if "attempts" in request.session:
        request.session.flush()
    return redirect('/random_word/')