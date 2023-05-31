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
    return for_return(politicianModel.getDetail({"id": p_id}))


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
    content = get_POST_data(request)
    cond = ["user_id", "policy_id", "ps_id", "remark"]
    result = checkParm(cond, content)
    if(isinstance(result,dict)):
        politicianModel.score(
            content["user_id"], content["policy_id"], content["ps_id"], content["remark"])
        return ret({"success": True, "message": "評分成功"})
    else:
        return ret({"success": False, "message": result})
