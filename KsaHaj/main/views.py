from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse

# Create your views here.
def mode_view(request:HttpRequest,mode):
    res=redirect(request.GET.get("next","/"))# "/": for defult query
    if mode=="light":
        res.set_cookie("mode","light")
    elif mode=="dark":
        res.set_cookie("mode","dark")
    return res

def dropdown_view(request:HttpRequest,state):
    res=redirect(request.GET.get("next","/"))
    if state=="open":
        res.set_cookie("state","open")
    elif state=="close":
        res.set_cookie("state","close")
    return res

def home_view(request:HttpRequest):
    return render(request,"main/home.html")

def kings_view(request:HttpRequest):
    return render(request,"main/kings.html")

def security_view(request:HttpRequest):
    return render(request,"main/security.html")

def health_view(request:HttpRequest):
    return render(request,"main/health.html")

def organization_view(request:HttpRequest):
    return render(request,"main/organization.html")

def technology_view(request:HttpRequest):
    return render(request,"main/technology.html")

def services_view(request:HttpRequest):
    return render(request,"main/services.html")