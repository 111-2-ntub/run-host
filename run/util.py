from flask import Response, jsonify, make_response
import json
from .coder import MyEncoder


def checkParm(cond, content, option=None):
    content=json.loads(content)
    res = ""
    result = {}
    for i in cond:
        if(i not in content):
            res += "缺少必要參數 %s\n" % i
            break
        else:
            result[i] = content[i]
    return res if len(res) > 0 else result


def ret(result):
    # print(result)
    mes= " " if "mes"  not in result.keys() else result["mes"]
    resultData = result["data"] if "data" in result else {}
    return json.dumps({"D": resultData, "message": mes, "success": result["success"], }, cls=MyEncoder)

def get_POST_data(requset):
    content = requset.body
    return json.loads(content)

def for_return(result):
    return json.loads(json.dumps(result,cls=MyEncoder))



# 好像不能用


def normalize_query_param(value):
    """
    Given a non-flattened query parameter value,
    and if the value is a list only containing 1 item,
    then the value is flattened.

    :param value: a value from a query parameter
    :return: a normalized query parameter value
    """
    return value if len(value) > 1 else value[0]


def normalize_query(params):
    """
    Converts query parameters from only containing one value for each parameter,
    to include parameters with multiple values as lists.

    :param params: a flask query parameters data structure
    :return: a dict of normalized query parameters
    """
    params_non_flat = params.to_dict(flat=False)
    return {k: normalize_query_param(v) for k, v in params_non_flat.items()}





def group(data: dict, tag: list, identity: str):
    
    """
    data 是原始資料
    tag 是要被處理成陣列的屬性
    identity是識別data是否為同一組ex id
    """
    tags = []
    ret = []
    for i in range(len(tag)):
        tags.append(set())
    check_id = -1
    temp={}
    for i in data:        
        if i[identity] != check_id:                        
            if check_id != -1:                
                for j in range(len(tag)):
                    temp[tag[j]] = tags[j]
                ret.append(temp)
            check_id = i[identity]
            temp = i
            tags.clear()
            for j in range(len(tag)):
                tags.append(set())
            else:                
                temp = i
        for j in range(len(tag)):              
            tags[j].add(i[tag[j]])
    for j in range(len(tag)):
        temp[tag[j]] = tags[j]
    ret.append(temp)
    return ret