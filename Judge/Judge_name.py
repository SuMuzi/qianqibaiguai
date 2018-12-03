from DBHelper.MysqldbHelper import mysqlhelper

def Isname(param):
    sql="select password from user where name=%s"
    db=mysqlhelper()
    rs=db.select_psword(sql,param)
   # print(rs)
    if not rs:
        #print("数据库中没有")
        return False
    else:
        #print("数据库中有")
        return True