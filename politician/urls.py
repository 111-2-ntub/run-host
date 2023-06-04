from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('list',views.list),# No error
	path('d/<str:p_id>',views.detail),
    path('area',views.area),# No error
    path("name",views.name),# No error
    path('term',views.term),# No error
    path('cond',views.cond),# No error
    # path('score/',views.getscore),  #GET
    path('score',views.score),  
]
