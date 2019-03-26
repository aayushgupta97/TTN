from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout

def index(request):
	if request.user.is_superuser:
		user_is = 'is super'
	elif request.user.is_staff:
		user_is = 'is staff'
	else:
		user_is = 'not logged in'
	return render(request, 'userauth/index.html' , {'user_is': user_is})

def user_logout(request):
	logout(request)
	return HttpResponse('<h1> you\'re logged out </h1>')