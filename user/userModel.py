# coding=utf-8
from run.db import DB
import json
from run.util import (group)

from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class MyUser(AbstractBaseUser):
    id=models.CharField(max_length=40,primary_key=True)
    name = models.CharField(max_length=40, unique=True)
    identity=models.IntegerField()
    class Meta:
        db_table="user"
    USERNAME_FIELD = 'name'

# def login(account, password):
#     sqlstr = f"select * from user where id=\"{account}\" and password = md5(\"{password}\")"
#     return (DB.execution(DB.select, sqlstr))

def del_user(account):
    try:
        record = MyUser.objects.get(id = account)
        result=record.delete()
        return {"message":"刪除成功","data":result}
    except:
        return {"message":"帳號不存在"}
        
    
        
    

def findPasswordByAccount(account, psw):
    sqlstr = f"select * from user where id=\"{account}\" and password=md5(\"{psw}\")"
    return DB.execution(DB.select, sqlstr)


def changePassword(account, password):
    sqlstr = f"update user set password = md5(\"{password}\") where id = \"{account}\""
    return DB.execution(DB.update, sqlstr)


def sign(account, password, age, gender, area, name, degree,phone):
    sqlstr = f"insert into user(id, password,birthday,gender,area_id,name,degree,phone) VALUES (\"{account}\", md5(\"{password}\") ,\"{age}\" ,\"{gender}\",\"{area}\",\"{name}\",\"{degree}\",\"{phone}\")"
    return DB.execution(DB.create, sqlstr)


def changeProfile(data, account):
    strCond = ""
    if(isinstance(data, dict)):
        for i in data.keys():
            strCond += f" {i} = \"{data[i]}\" ,"
    sqlstr = f"update user set {strCond[0:len(strCond)-1]} where id=\"{account}\""
    return DB.execution(DB.update, sqlstr)


# def findArea(area):
#     sqlstr = "select * from area "
#     return DB.execution(DB.select, sqlstr)


def findUserarea(area):
    sqlstr = f"select area from user where id = \"{area}\""
    return DB.execution(DB.select, sqlstr)


def hasUser(userid):
    sqlstr = f"select count(*) as c from user where id=\"{userid}\""
    return DB.execution(DB.select, sqlstr)


def user(user_id):
    sqlstr = [
        {"sql": "".join(["SELECT u.id,u.name,degree,a.name as a_n ,gender,birthday,line FROM user as u join area as a on u.area_id=a.id where u.id=\"", user_id, "\""]), "name": "user"},
        {"sql": "select * from area", "name": "area"},
      
      
        {
            "sql": "".join(["select p.*,s.name as type ,c.name as c_name from user_policy  as up  join policy as p on up.policy_id=p.id join schedule as s on up.ps_id=s.id join policy_category as pc on pc.policy_id=p.id join category as c on pc.category_id=c.id where user_id=\"", user_id, "\" group by up.id,p.id,c.id "]),
            "name": "policy_vote"
        },
       {
            "sql": f"SELECT c.* FROM user_category as uc join category as c on uc.category_id=c.id where userid=\"{user_id}\"", "name": "category"
        }

    ]
    data = DB.execution(DB.select, sqlstr)

 
    data["data"]["policy_vote"] = group(
        data["data"]["policy_vote"], ["c_name"], "id")

    return data


def getUserIdByLine(line_id):
    sqlstr = f"select id from user where line=\"{line_id}\""
    data = DB.execution(DB.select, sqlstr)
    return str(data["data"][0]["id"].decode())


def getUserByLine(line_id):
    sqlstr = f"select * from user where line=\"{line_id}\""
    return DB.execution(DB.select, sqlstr)


def setCateogry(user_id, add, remove):
    sqlstrs = []
    if len(add) > 0:
        for i in add:

            sqlstrs.append(
                {"sql": f"insert into user_category (user_id,category_id) values(\"{user_id}\",{i}) ; "})
    removes = []

    if len(remove) > 0:
        for i in remove:
            removes.push(f"{i}")
        delStr = f"delete user_category where user_id=\"{user_id}\" and category_id in ({' , '.join(removes)})"
        sqlstrs.append({"sql": delStr})
    return DB.execution(DB.create, sqlstrs)


def politician_user(p_id):
    sqlstr = [
        {
            "sql":

            "SELECT p.id,p.term,f.name,p.photo,a.name as a_n,p.experience,p.degree,p.tel,pa.name as p_name,e.name as e_n,e.remark"
            + " FROM politician as p join electorate as e on p.electorate_id=e.id join figure as f on p.figure_id=f.id join area as a on e.area_id=a.id join party as pa on p.party_id=pa.id"
            + f" where p.id=\" {p_id} \" order by e.area_id,p.term,f.name", "name": "detail"
        }, {
            "sql": "".join(["SELECT * FROM count_score where  id =\"", p_id, "\""]), "name":"count_score"
        }, {
            "sql": f"SELECT * FROM policy_top where politician_id={p_id} limit 3",
            "name": "policy"
        }, {
            "sql": f"SELECT * FROM proposal_top where id={p_id} limit 3", "name": "proposal"
        }, {
            "sql": f"select sum(postive)/count(*) as score from message as m join proposal as p on m.proposal_id=p.id join proposer as er on p.id=er.proposal_id where er.politician_id={p_id}", "name": "message"
        }, {
            "sql": f"select s.*,count(s.id)  as score from user_proposal as up join proposal as p on p.id =up.proposal_id join proposer as er on er.proposal_id=p.id right join stand as s on stand_id=s.id where er.politician_id={p_id} group by s.id", "name": "stand"
        }, {
            "sql": f"SELECT le.committee_id,le.politician_id,com.name FROM legislatorcol as le join politician as p on le.politician_id = p.id join committee as com on le.committee_id=com.id where politician_id = {p_id} group by politician_id", "name": "committee"
        }
    ]
    return DB.execution(DB.select, sqlstr)
