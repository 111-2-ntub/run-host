from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('/',views.find),
	path('msg/',views.msg),
    path('<p_id>/',views.search),
    path("vote/",views.vote),
    path("save/",views.save),
    path("report/",views.report),
    path("rule/",views.rule),
    path("cond/",views.cond),
    path("great/",views.report),
    path("save/del/",views.removeSave),
]
