from django.db import models

# Create your models here.

class Employee(models.Model):
	name = models.CharField(max_length = 50)
	age = models.IntegerField()
	salary = models.IntegerField()
	created_date = models.DateTimeField(auto_now_add = True)
	modified_date = models.DateTimeField(auto_now = True)
	reporting_manager = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
	designation_choices = [('developer', 'developer'), ('Project Manager', 'Project Manager'), ('Trainee', 'Trainee')]
	designation = models.CharField(max_length = 50, choices = designation_choices)
