from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.
def func0(request):
	return HttpResponse("You are at the app1")

def func1(request):
	mydict={'insert_me':"hey i come from django"}
	return render(request, 'app1/display.html',context=mydict)

def func2(request):
	return HttpResponse("You are at the app1 page2")
