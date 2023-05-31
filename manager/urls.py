from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('identity/',views.identity),
	path('user/',views.identityUser),
    path('report/',views.report)
]
