# coding=utf-8
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from . import runModel
from run.util import (ret,checkParm,get_POST_data,for_return)
import json

def home(request):
    return JsonResponse(for_return(runModel.home()))
