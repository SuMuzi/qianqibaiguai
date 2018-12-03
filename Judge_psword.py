from DBHelper.MysqldbHelper import mysqlhelper

def IsPaaword(param):
    sql="select password from user where name=%s"
    db=mysqlhelper()
    rs=db.select_psword(sql,param)
   # print(rs)
    return rs[0]