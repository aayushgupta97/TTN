from django.contrib import admin
from django.urls import path
from appone import views as app_one_view
from apptwo import views as app_two_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:input_num>',app_two_view.MyView.as_view(),name='function_two'),
    path('<filename>',app_one_view.function_one,name='function_one')
]