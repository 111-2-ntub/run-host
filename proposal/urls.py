from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.find), # TypeError(f'the JSON object must be str, bytes or bytearray, ' TypeError: the JSON object must be str, bytes or bytearray, not dict
	path('msg/',views.msg), # TypeError(f'the JSON object must be str, bytes or bytearray, ' TypeError: the JSON object must be str, bytes or bytearray, not dict
    path('<str:p_id>/',views.search), # user_id? get.args?
    path("vote/",views.vote), # proposal_vote 資料表?
    path("save/",views.save), #
    path("report/",views.report),
    path("rule/",views.rule),
    path("cond/",views.cond),
    path("great/",views.report),
    path("save/del/",views.removeSave),
]
