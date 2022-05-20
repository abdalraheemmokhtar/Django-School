from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import InputForm
from django.urls import reverse

# Create your views here.
def student(request):
    return render(request, 'student.html',{})

def register(request):
    return render(request, 'register.html', {})


# Create your views here.
def home_view(request):
    context ={}
    context['form']= InputForm()
    return render(request, "login.html", context)

def perform_login(request):
    if request.method != 'POST':
        return HttpResposnse("Method not allowed")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_obj = authenticate(request, username=username, password = password)
        if user_obj is not None:
            login(request, user_obj)
            return HttpResponseRedirect(reverse("admin_dashboard"))
        else:
            return HttpResponseRedirect('/cus')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')