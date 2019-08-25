from django.shortcuts import render
from api.models import *
import requests
# Create your views here.

def indexView(request):
    return render(request,'index.html')

def elementsView(request):
    context = {}
    if 'token' not in request.GET:
        return render(request,'index.html')
    headers = {
        'Authorization': 'Token ' + request.GET['token']
    }
    r = requests.get('https://nishantwrp.herokuapp.com/api/students/',headers=headers)
    context['students'] = r.json()
    context['token'] = request.GET['token']
    return render(request,'elements.html',context=context)

def studentDetailsView(request,pk):
    context = {}
    if 'token' not in request.GET:
        return render(request,'index.html')
    headers = {
        'Authorization': 'Token ' + request.GET['token']
    }
    r = requests.get('https://nishantwrp.herokuapp.com/api/students/',headers=headers)
    for obj in r.json():
        if obj['id'] == pk:
            context['student'] = obj
            break
    return render(request,'studentdetails.html',context=context)

def enterMarksView(request):
    context = {}
    if 'token' not in request.GET:
        return render(request,'index.html')
    headers = {
        'Authorization': 'Token ' + request.GET['token']
    }
    r = requests.get('https://nishantwrp.herokuapp.com/api/students/',headers=headers)
    context['students'] = r.json()
    context['token'] = request.GET['token']
    context['length'] = len(r.json())
    return render(request,'entermarks.html',context=context)

def addView(request):
    context = {}
    if 'token' not in request.GET:
        return render(request,'index.html')
    headers = {
        'Authorization': 'Token ' + request.GET['token']
    }
    return render(request,'add.html',context=context)

def loginView(request):
    context = {}
    if 'registered' in request.GET:
        context['registered'] = True
    return render(request,'login.html',context=context)

def registerView(request):
    context = {}
    return render(request,'register.html',context=context)