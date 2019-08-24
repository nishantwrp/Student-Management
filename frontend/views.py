from django.shortcuts import render

# Create your views here.

def indexView(request):
    return render(request,'index.html')

def kuttaView(request):
    return render(request,'elements.html')

def genView(request):
    return render(request,'generic.html')

def loginView(request):
    return render(request,'login.html')

def registerView(request):
    return render(request,'register.html')