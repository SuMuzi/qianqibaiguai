import pymysql

class mysqlhelper:

    def getCon(self):
        try:
            conn = pymysql.connect(host='localhost', user='root', passwd='mysql', db='test', port=3306, charset='utf8')
            #print("数据库连接成功")
            return conn
        except pymysql.Error as e:
            print("数据库连接失败,%s"% e)

    def select(self,sql):
        try:
            con=self.getCon()
            #print(con)
            #cur = con.cursor(pymysql.cursors.DictCursor)
            cur=con.cursor()
            cur.execute(sql)
            fc=cur.fetchall()
            return fc
        except pymysql.Error as e:
            print("查询失败，请检查数据库！,%s"% e)
        finally:
            cur.close()
            con.close()

    def select_psword(self, sql,param):
        try:
            con = self.getCon()
            # print(con)
            #cur = con.cursor(pymysql.cursors.DictCursor)
            cur = con.cursor()
            cur.execute(sql,param)
            fc = cur.fetchone()
            return fc
        except pymysql.Error as e:
            print("查询失败，请检查数据库！,%s" % e)
        finally:
            cur.close()
            con.close()
    def update(self, sql, params):
        try:
            con = self.getCon()
            print(con)
            cur = con.cursor()
            count = cur.execute(sql, params)
            con.commit()
            #print("更新成功")
            return count
        except pymysql.Error as e:
            print("更新失败，请检查数据库！,%s"% e)

        finally:
            cur.close()
            con.close()



