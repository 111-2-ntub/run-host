from .db import DB


def home():
    sqlstr = [{"sql": "select * from home_policy limit 5", "name": "policy"},
              {"sql": "select  cs.name,round(cs.score,2) as score,p.photo from count_score as cs join politician as p on cs.id=p.id order by score desc limit 3", "name": "rank"}]
    result = DB.execution(DB.select, sqlstr)
    return result