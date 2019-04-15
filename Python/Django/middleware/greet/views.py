from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.
def hello(request):
    context = {
        'name' : "Aayush",
        'footer': 'footer'
    }
    return TemplateResponse(request, 'greet/greeting.html', context)
