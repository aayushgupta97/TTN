from django.shortcuts import render
from django.http import HttpResponse
from collections import defaultdict
import sys


def wish_user(request,input_num):
    if input_num in range(6,12):
        wish = 'Good Morning'
    elif input_num >= 12 and input_num < 18:
        wish = 'Good Evening'
    elif input_num >= 18 and input_num < 24:
        wish = 'Good Night'
    else:
        wish = 'Go To Bed'
    #return HttpResponse(wish)
    return wish


def multiply(a, b):
    return a * b
