from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader
# Create your views here.
def members(request):
    a ="myfirst.html"
    return render (request,'myfirst.html', {'a':a})
