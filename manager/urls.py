from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('identity',views.identity), # No error
	path('user',views.identityUser), # No error
    path('report',views.report) # No error
]
