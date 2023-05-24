from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login),
    path('sign/',views.sign),
    path("u/<str:u_id>/",views.getUser),
    path('/',views.user),
    path('psw/',views.edit),
    path('category/',views.c),
	path('p_user/<str:p_id>',views.p_user)
]
