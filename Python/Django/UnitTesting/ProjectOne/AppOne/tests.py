from django.test import TestCase
from django.http import HttpResponse

from .views import function_one
# from .views import multiply, wish_user
import unittest
from  django.test.client import RequestFactory
# Create your tests here.

class ComplexTest(unittest.TestCase):
    
    def setUp(self) -> None:
        self.factory = RequestFactory()
        
    def test_one(self):
        """will pass if a file named 'file' exist otherwise fail"""
        request = self.factory.get('')
        response = function_one(request, 'file')
        self.assertEqual(response.status_code, 200)
        
    def test_two(self):
        """Will pass as no file_two exists"""
        request = self.factory.get('')
        response = function_one(request, 'file_two')
        self.assertNotEqual(response, HttpResponse('no such file found')) # what the function returns, comparing it with response
        
    def test_three(self):
        """Will fail"""
        request = self.factory.delete('')
        response = function_one(request, 'file_two')
        self.assertEqual(response, HttpResponse('file deleted successfully'))
    
    