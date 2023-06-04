from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login),  #
    path('sign',views.sign),
    path("u/<str:u_id>",views.user), # No error
    path('',views.user), # No error
    path('psw',views.edit),# No error
    # path('category/',views.c), #新增使用者感興趣的類別
	# path('p_user/<str:p_id>',views.p_user)# 查詢政治人物使用者
]
