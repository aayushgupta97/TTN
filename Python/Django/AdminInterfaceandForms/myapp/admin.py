from django.contrib import admin
from .models import Manager, Employee
# Register your models here.

class ManagerAdmin(admin.ModelAdmin):
	list_display = ('Name', 'Age', 'Department', 'created_date', 'modified_date')
	list_filter = ('Age', )
	list_editable = ('Department', )


class EmployeeAdmin(admin.ModelAdmin):
	list_display = ('Name', 'Age', 'Salary', 'Designation', 'reporting_manager', 'created_date', 'modified_date')
	list_filter = ('Age', 'Salary')
	search_fields = ('Name',)
	fieldsets = ( 
			('Personal information', {
				'fields' : ('Name', 'Age', )
				}),
			('Work information', {
				'fields' : ('Salary', 'Designation', )
				}),
			('Manager', {
				'fields' : ('reporting_manager', )
				})
		)


admin.site.register(Manager, ManagerAdmin)
admin.site.register(Employee, EmployeeAdmin)



