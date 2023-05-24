from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login),
    path('sign/',views.sign),
    path("<int:u_id>/",views.getUser),
    path('/',views.user),
    path('psw/',views.edit),
    path('category/',views.c),
	path('p_user/<int:p_id>',views.p_user)
]
