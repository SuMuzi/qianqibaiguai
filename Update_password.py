from DBHelper.MysqldbHelper import mysqlhelper
#from Judge.Judge_id import Isid

def update_password(params):
    sql = "update user set password=%s where name=%s"
    db=mysqlhelper()
    #if Isid(id):
    db.update(sql, params)
    return True
    #else:
      # return False
if __name__ == '__main__':
    update_password(("123","阿萨德"))