
from django.template.response import TemplateResponse
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, render

from greet.views import hello


class Footer:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        response = hello(request)
        response.context_data['footer'] = 'Made by : Aayush Gupta'
        return response