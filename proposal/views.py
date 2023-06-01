# coding=utf-8
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from . import proposalModel
from run.util import (ret,checkParm,get_POST_data,for_return,normalize_query)
import json
from django.contrib import auth


def find(request):
    cond = ["id", "term",  "status_id", "title"]
    content = request.args
    after = normalize_query(content)
    condData = {}
    for i in after.keys():
        if i in cond:
            condData[i] = after[i]
    data = {}
    data["cond"] = condData
    data["page"] = after["page"] if "page" in after.keys() else 0
    # for i in cond:

    return ret(proposalModel.pList(data))


def msg(request):
    print("here")
    content = request.json
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
    return ret(data)


def search(p_id,request):
    user_id = request.args.get("user_id")
    return ret(proposalModel.msgList(p_id, user_id))


def vote(request):
    content = request.json
    cond = ["user_id", "sp_id", "proposal_id"]
    t = checkParm(cond, content)
    if(isinstance(t, str)):
        data = {"success": False, "mes": t}
    else:
        data = proposalModel.vote(
            userid=content[cond[0]], sp_id=content[cond[1]], proposal_id=content[cond[2]])
    return ret(data)


def save(request):
    if request.method =="GET":
        content = request.json
        cond = ["user_id", "proposal_id"]
        result = checkParm(cond, content)
        if(isinstance(result, dict)):
            return ret(proposalModel.save(content["user_id"], content["proposal_id"]))
        else:
            return ret({"success": False, "message": result})
    else:
        content = request.args.get("user_id")
        cond = ["user_id"]
        # result = checkParm(cond, content)
        if(content == ""):
            return ret({"success": False, "message": "請登入"})
        else:
            return ret(proposalModel.getSave(content))



def report(request):
    content = request.json
    cond = ["user_id", "message_id", "remark", "rule"]
    t = checkParm(cond, content)
    if(isinstance(t, dict)):
        return ret(proposalModel.report(content["user_id"], content["message_id"], content["remark"], content["rule"]))
    else:
        return ret({"success": False, "message": t})


def rule():
    return ret(proposalModel.rule())


def cond():
    return ret(proposalModel.getCond())


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
        return ret(proposalModel.removeSave(t["user_id"], t["proposal_id"]))
    else:
        return ret({"success": False, "message": t})