from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
# def wish_user(request,input_num):
# 	if input_num >=0 and input_num <= 24:
# 	    if 5 < input_num and input_num < 12:
# 	        wish='Good Morning'
# 	    elif 12 <= input_num and input_num < 18:
# 	        wish='Good Evening'
# 	    elif 18 <= input_num and input_num < 24:
# 	        wish='Good Night'
# 	    else:
# 	        wish='Go To Bed'
# 	    return HttpResponse(wish)
# 	else: 
# 		return HttpResponse("Invalid Time try again!")

class MyView(View):
	def get(self, request, input_num):
		if input_num >=0 and input_num <= 24:
		    if 5 < input_num and input_num < 12:
		        wish='Good Morning'
		    elif 12 <= input_num and input_num < 18:
		        wish='Good Evening'
		    elif 18 <= input_num and input_num < 24:
		        wish='Good Night'
		    else:
		        wish='Go To Bed'
		    return HttpResponse(wish)
		else: 
			return HttpResponse("Invalid Time try again!")