from django.shortcuts import render
from django.http import HttpResponse
from . import politicianModel
from ...runapp import util
from flask import request

ret = util.ret
checkParm = util.checkParm
normalize_query = util.normalize_query


def list():
    print(request.args.get("name"))
    data = request.args
    query_params = normalize_query(data)
    print(query_params)
    return ret(politicianModel.getList({}))


def detail(p_id):
    return ret(politicianModel.getDetail({"id": p_id}))


def area():
    return ret(politicianModel.getArea())


def name():
    return ret(politicianModel.getName())


def term():
    return ret(politicianModel.getTerm())


def cond():
    return ret(politicianModel.getCond())



def getScore():
    return ret(politicianModel.schedule())


def score():
    content = request.json
    cond = ["user_id", "policy_id", "ps_id", "remark"]
    result = checkParm(cond, content)
    if(isinstance(result,dict)):
        politicianModel.score(
            content["user_id"], content["policy_id"], content["ps_id"], content["remark"])
        return ret({"success": True, "message": "評分成功"})
    else:
        return ret({"success": False, "message": result})
