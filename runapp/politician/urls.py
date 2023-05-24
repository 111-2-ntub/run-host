from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.list),
	path('<int:p_id>/',views.detail),
    path('area/',views.area),
    path("name/",views.name),
    path('term/',views.term),
    path('cond/',views.cond),
    path('score/',views.getscore),  #GET
    # path('score/',views.score),  POST
]
