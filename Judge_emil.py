from DBHelper.MysqldbHelper import mysqlhelper

def Isemail(param):
    sql="select password from user where email=%s"
    db=mysqlhelper()
    rs=db.select_psword(sql,param)
   # print(rs)
    if not rs:
        #print("数据库中没有")
        return False
    else:
        #print("数据库中有")
        return True

if __name__ == '__main__':
    Isemail("1013719026@qq.com")