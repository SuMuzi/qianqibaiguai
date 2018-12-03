from DBHelper.MysqldbHelper import mysqlhelper
from Judge.Judge_id import Isid

def insert_new(params,id):
    sql = "insert into user values (%s,%s,%s,%s)"
    db=mysqlhelper()
    if Isid(id):
       db.update(sql, params)
       return True
    else:
       return False


if __name__ == '__main__':

  if insert_new(("2111","2222","3333","4444"),"2111"):
    print("False")
  else:
    print("True")

