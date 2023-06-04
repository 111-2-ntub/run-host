from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . import politicianModel
from  run.util import(ret,checkParm,get_POST_data,group,for_return)
# from flask import request

# ret = util.ret
# checkParm = util.checkParm
# normalize_query = util.normalize_query


def list(request):
    return JsonResponse(for_return(politicianModel.getList({})))


def detail(request,p_id):
    return JsonResponse(for_return(politicianModel.getDetail({"id": p_id})))


def area(request):
    return JsonResponse(for_return(politicianModel.getArea()))


def name(request):
    return JsonResponse(for_return(politicianModel.getName()))


def term(request):
    return JsonResponse(for_return(politicianModel.getTerm()))


def cond(request):
    return JsonResponse(for_return(politicianModel.getCond()))



def getScore(request):
    return JsonResponse(for_return(politicianModel.schedule()))


def score(request):
    if request.method =="GET":
        return JsonResponse(for_return(politicianModel.schedule()))
    else:
        cond = ["user_id", "policy_id", "ps_id", "remark"]
        result = checkParm(cond, request.body)
        if(isinstance(result,dict)):
            politicianModel.score(
                result["user_id"], result["policy_id"], result["ps_id"], result["remark"])
            return JsonResponse({"success": True, "message": "評分成功"})
        else:
            return JsonResponse({"success": False, "message": result})
