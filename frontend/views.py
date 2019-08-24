from django.shortcuts import render

# Create your views here.

def indexView(request):
    return render(request,'index.html')

def elementsView(request):
    return render(request,'elements.html')

def genView(request):
    return render(request,'generic.html')

def loginView(request):
    context = {}
    if 'registered' in request.GET:
        context['registered'] = True
    return render(request,'login.html',context=context)

def registerView(request):
    context = {}
    return render(request,'register.html',context=context)