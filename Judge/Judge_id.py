from DBHelper.MysqldbHelper import mysqlhelper

def Isid(param):
    sql="select password from user where name=%s"
    db=mysqlhelper()
    rs=db.select_psword(sql,param)
   # print(rs)
    if not rs:
        return True
    else:
        return False
#Isid("www")
#Isid("qqqq")