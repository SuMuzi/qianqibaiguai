from DBHelper.MysqldbHelper import mysqlhelper



sql="delete from user where name=%s"
sql2="insert into user values (%s,%s,%s,%s)"
sql3="select password from user where name ='asd'"
db=mysqlhelper()
db.update(sql2,('qqqqqqqqqqq','asd','123456','wqwqwqw'))
print(db.select_psword(sql3))
if db.select_psword(sql3)=="asd":
    print("True")
else:
    print("False")
if db.select_psword(sql3)[0] == "asd":
    print("True2")
else:
    print("False2")
print(db.select_psword(sql3)[0])
print(db.select(sql3))

