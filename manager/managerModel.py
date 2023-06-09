from run.db import DB
import json
from run.util import (group)
from datetime import datetime

def setIdentity(user_id, identity):
    sqlstr = f"update user set identity={identity} where id=\"{user_id}\""
    return DB.execution(DB.update, sqlstr)


def identity():
    sqlstr = "select * from identity"
    return DB.execution((DB.select), sqlstr)


def getUser():
    sqlstr = [
        {"sql": "select * from user where identity=1", "name": "user"},
        {"sql": "select * from user where identity=2", "name": "manager"},
        {"sql": "select * from user where identity=3", "name": "politician"},
        {"sql": "select * from identity", "name": "identity_type"}
    ]
    return DB.execution(DB.select, sqlstr)


def reportCheck(check, report_id, manager_id, time):
    sqlstr = "update report set `check`=%s where `id`=%s" % (
            check, report_id)
    if(check == 0 ):
        return DB.execution(DB.update, sqlstr)
        
    elif(check == 1):
        time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        sqlstr + "insert into freezen (manager_id,report_id,time) values(%s,%s,%s)" % (
            manager_id, report_id, time)
        return DB.execution(DB.update, sqlstr)


def report():
    sqlstr = [{"name": "already", "sql": "select  r.*,m.content from report as r join message as m on r.message_id= m.id where r.check =1"},
                {"name": "not_yet", "sql": "select  r.*,m.content from report as r join message as m on r.message_id= m.id where r.check=0"}]
    return DB.execution(DB.select, sqlstr)
