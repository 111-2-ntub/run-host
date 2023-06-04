from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.find), #
	path('msg/',views.msg), # 
    path('<str:p_id>/',views.search), # user_id?
    path("vote/",views.vote), # proposal_vote 資料表?
    path("save/",views.save), #
    path("report/",views.report),
    path("rule/",views.rule),
    path("cond/",views.cond),
    path("great/",views.report),
    path("save/del/",views.removeSave),
]
