# coding=utf-8
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from . import proposalModel
from run.util import (ret,checkParm,get_POST_data,for_return,normalize_query)
import json
from django.contrib import auth
from proposal.filter import (DFAFilter)
from run.coder import MyEncoder 


def find(request):
    cond = ["id", "term",  "status_id", "title"]
    content = request.GET
    # print(content)
    # after = normalize_query(content)
    t = checkParm(cond, content)
    condData = {}
    for i in t.keys():
        if i in cond:
            condData[i] = t[i]
    data = {}
    data["cond"] = condData
    data["page"] = t["page"] if "page" in t.keys() else 0
    # for i in cond:

    return JsonResponse(for_return(proposalModel.pList(data)))


def msg(request):
    print("here")
    content = get_POST_data(request)
    cond = ["user_id", "content", "article_id", "parent_id"]
    t = checkParm(cond, content)
    if(isinstance(t, dict)):
        gfw = DFAFilter()
        gfw.parse()
        text = content["content"]
        result = gfw.filter(text)
        if len(str(content["content"]).replace("*", "")) == len(str(result).replace("*", "")):
            data = proposalModel.msg(
                account=content[cond[0]], mes=content[cond[1]], article_id=content[cond[2]], parent_id=content[cond[3]])
        else:
            data = {"success": False, "mes": "請確認是否有不雅字詞出現"}
    else:
        data = {"success": False, "mes": t}
    return JsonResponse(json.dumps(data),cls=MyEncoder)


def search(request,p_id):
    # user_id = request.args.get("user_id")
    print(json.loads(request.body))
    return JsonResponse(for_return(proposalModel.msgList(p_id, user_id)))


def vote(request):
    content = get_POST_data(request)
    cond = ["user_id", "sp_id", "proposal_id"]
    t = checkParm(cond, content)
    if(isinstance(t, str)):
        data = {"success": False, "mes": t}
    else:
        data = proposalModel.vote(
            userid=content[cond[0]], sp_id=content[cond[1]], proposal_id=content[cond[2]])
    return JsonResponse(for_return(data))


def save(request):
    if request.method =="GET":
        content = request.body
        print(json.loads(content))
        cond = ["user_id", "proposal_id"]
        result = checkParm(cond, content)
        if(isinstance(result, dict)):
            return JsonResponse(for_return(proposalModel.save(content["user_id"], content["proposal_id"])))
        else:
            return JsonResponse(for_return({"success": False, "message": result}))
    else:
        content = request.args.get("user_id")
        cond = ["user_id"]
        # result = checkParm(cond, content)
        if(content == ""):
            return JsonResponse(for_return({"success": False, "message": "請登入"}))
        else:
            return JsonResponse(for_return(proposalModel.getSave(content)))



def report(request):
    content = request.json
    cond = ["user_id", "message_id", "remark", "rule"]
    t = checkParm(cond, content)
    if(isinstance(t, dict)):
        return JsonResponse(for_return(proposalModel.report(content["user_id"], content["message_id"], content["remark"], content["rule"])))
    else:
        return JsonResponse(for_return({"success": False, "message": t}))


def rule():
    return JsonResponse(for_return(proposalModel.rule()))


def cond():
    return JsonResponse(for_return(proposalModel.getCond()))


def great(request,m_id):
    if request.method =="POST":
        checkParm(["user_id", "m_id"])
        sqlstr = ""
    elif request.method =="DELETE":
        sqlstr = f"select * from great where id={m_id}"
    else:
        checkParm(["m_id"])
        return ""



def removeSave(request):
    content = request.json
    cond = ["user_id", "proposal_id"]
    t = checkParm(cond, content)
    if(isinstance(t, dict)):
        return JsonResponse(for_return(proposalModel.removeSave(t["user_id"], t["proposal_id"])))
    else:
        return JsonResponse(for_return({"success": False, "message": t}))