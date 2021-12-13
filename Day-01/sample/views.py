from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def demo(request):
	return HttpResponse("<h1 style='color:green'>hello world</h1>")

def state(request,y):
	return HttpResponse("Hi Welcome {}".format(y))
