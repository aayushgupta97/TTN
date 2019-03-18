from django.shortcuts import render,HttpResponse
from datetime import datetime

# Create your views here.

def greetings(request):
	if datetime.now().hour > 12 :
		return HttpResponse("Good Evening")
	else :
		return HttpResponse("Good Morning")