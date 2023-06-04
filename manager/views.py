from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from . import managerModel
from run.util import (ret,checkParm,for_return)
from run.coder import MyEncoder 
import json


def identity(request):
    if request.method =="GET":
        print("get")
        result=managerModel.identity()
        print(result)
        return JsonResponse(for_return(result))
    else:
        print("post")
        content = request.body
        print(json.loads(content))
        cond = ["user_id", "identity"]
        t = checkParm(cond,content)
        if(isinstance(t, dict)):
            return JsonResponse(for_return(managerModel.setIdentity(t["user_id"], t["identity"])))
        else:
            return JsonResponse({"success": False, "message": t})

# 未完成
# 轉身分
    

def identityUser(request):
    if request.method=="GET":
        return JsonResponse(for_return(managerModel.getUser()))
    else:
        return JsonResponse(for_return(managerModel.report()))


# 檢舉審核
def report(request):
    if request.method =="GET":
        return JsonResponse(for_return(managerModel.report()))
    else:
        content = request.body  
        cond = [ "check","report_id","manager_id","time"]
        t = checkParm(cond, content)
        print(t)
        if(isinstance(t, dict)):
            data = managerModel.reportCheck(
            check=t["check"], report_id=t["report_id"], manager_id=t["manager_id"],time=t["time"])
            return JsonResponse(for_return(data))
        else:
            return JsonResponse({"success": False, "message": t})