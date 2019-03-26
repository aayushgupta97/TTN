from django.shortcuts import render

# Create your views here.

def index(request):
	# Get a session value, setting a default if it is not present (default = 0)
	my_count = request.session.get('my_count', 0)
	my_count = my_count + 1
	# Save the session 
	request.session['my_count'] = my_count
	
	request.session.set_expiry(300)
	return render(request, 'djsession/index.html', {"counter":my_count})
