from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from . import managerModel
from run.util import (ret,checkParm)
from run.coder import MyEncoder 
import json


def identity(request):
    if request.method =="GET":
        print("get")
        result=managerModel.identity()
        print(result)
        return JsonResponse(json.dumps(
            result,cls=MyEncoder))
    else:
        print("post")
        content = request.json
        cond = ["user_id", "identity"]
        t = checkParm(cond,content)
        if(isinstance(t, dict)):
            return JsonResponse(json.dumps(managerModel.setIdentity(t["user_id"], t["identity"])))
        else:
            return JsonResponse(json.dumps({"success": False, "message": t}))

# 未完成
# 轉身分
    

def identityUser(request):
    if request.method=="GET":
        result=ret(managerModel.getUser())
        print("result")
        print(type(result))
        return JsonResponse(data= result)
    else:
        return JsonResponse(managerModel.report())


# 檢舉審核
def report(request):
    content = request.body  
    cond = [ "check","report_id","manager_id","time"]
    t = checkParm(cond, content)
    if(isinstance(t, dict)):
        data = managerModel.reportCheck(
            check=content[cond[0]], report_id=content[cond[1]], manager_id=content[cond[2]],time=content[cond[3]])
        return JsonResponse(data)
    else:
        return JsonResponse({"success": False, "message": t})