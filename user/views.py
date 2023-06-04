# coding=utf-8
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from . import userModel
from run.util import (ret,checkParm,get_POST_data,for_return)
import json
from django.contrib import auth

# ret = util.ret
# checkParm = util.checkParm

from django.contrib.auth.hashers import check_password



def authenticate(username=None, password=None):
    try:
        user = userModel.MyUser.objects.get(id=username)
        
        if password==user.password:
            return user
        return None
    except userModel.MyUser.DoesNotExist:
        # No user was found.
        return None

def login(request):
    print("enter login ")
    content=get_POST_data(request)
    username = content['username']
    password = content['password']
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:        
        return JsonResponse(for_return({"message":"login successfully","success":True,"data":{"identity":user.identity}}))
    else:
        return JsonResponse({"message":"login fail","success":False})
    # return JsonResponse("good")
    content = request.POST
    account = content['account']
    password = content["password"]
    data = userModel.login(account, password)
    result = {"success": False, "data": data}
    if len(data["data"]) == 1:
        result["mes"] = "登入成功"
        result["success"] = True
    elif len(data["data"]) == 0:
        result["mes"] = "登入失敗"
    else:
        result["mes"] = "登入異常"

    return (result)


def sign(request):
    content = request.POST
    cond = ["account", "password", "age", "sex",
            "areaid", "name", "degree", "phone"]
    result = {"success": False, "mes": ""}
    t = checkParm(cond, content)

    if(isinstance(t, dict)):
        data = userModel.sign(t["account"], t["password"],t["age"], t["sex"], t["areaid"], t["name"], t["degree"], t["phone"])
        if(data["success"]):
            result["mes"] = "註冊成功"
            result["success"] = True
        else:
            hasUser = userModel.hasUser(t["account"])["data"][0]["c"]
            if hasUser > 0:
                result["mes"] = f"註冊異常 - 重複帳號"
            else:
                result["mes"] = "註冊異常"
    else:
        result["mes"] = "請填畢所有資料"
    return JsonResponse(result)


def getUser(request,u_id):
    print('this is get user')
    return JsonResponse(userModel.hasUser(u_id),safe=False)


def user(request,u_id):
    
    # content = get_POST_data(request)
    result=userModel.user(u_id)
    return JsonResponse(for_return(result))


def edit(request):
    content = request.body
    print(json.loads(content))
    cond = ["account", "oldPassword", "password", "passwordConfire"]
    result = {"success": False, "mes": ""}
    t = checkParm(cond, content)
    
    if(isinstance(t, dict)):
        oldPasswordFromDB = userModel.findPasswordByAccount(
            t["account"], t["oldPassword"])
        print(f'this is idk{oldPasswordFromDB}')
        if(oldPasswordFromDB["success"]):
            oldPasswordFromDB = oldPasswordFromDB["data"]
            if(len(oldPasswordFromDB) > 0):
                if(t["password"] != t["passwordConfire"]):
                    result["mes"] += "密碼和確認密碼不同\n"
                if(result["mes"] == ""):
                    data = userModel.changePassword(
                        t["account"], t["password"])
                    result["mes"] = "更換密碼成功"
                    result["success"] = True
                    result["data"] = data
            elif(len(oldPasswordFromDB) == 0):
                result["mes"] = "輸入舊密碼錯誤"
            else:
                result["mes"] = "帳號異常"
    else:print("this is else")
    return JsonResponse((result))



def changeProfile(request):
    content = request.POST
    account = content["account"]
    cond = ["area_id", "name"]
    data = {}
    for i in cond:
        if(i in content.keys()):
            data[i] = content[i]
    data = userModel.changeProfile(data, account)
    result = {"success": False, "mes": "修改異常", "data": data}
    if(data["success"]):
        result["success"] = True
        result["mes"] = "修改成功"
    return JsonResponse((result))



def c(request):
    content = request.POST
    t = checkParm(["user_id", "add", "remove"],content)
    if isinstance(t, dict):
        return JsonResponse((userModel.setCateogry(t["user_id"], t["add"], t["remove"])))
    else:
        return JsonResponse(({"success": False, "mes": t}))


def p_user(request,p_id):
    return JsonResponse((userModel.politician_user(p_id)))
    