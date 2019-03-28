from django.db import models

# Create your models here.

class Manager(models.Model):
	Name = models.CharField(max_length =50)
	Age = models.IntegerField()
	Department = models.CharField(max_length=50)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.Name} / {self.Department}"


class Employee(models.Model):
	Name = models.CharField(max_length =50)
	Age = models.IntegerField()
	Salary = models.IntegerField()
	Designation = models.CharField(max_length=50)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)
	reporting_manager = models.ForeignKey(Manager, on_delete=models.DO_NOTHING)

	def __str__(self):
		return self.Name