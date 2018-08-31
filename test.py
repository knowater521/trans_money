#encoding:UTF-8
# import MySQLdb
#
# conn =MySQLdb.Connect(
#     host='127.0.0.1',
#     port=3306,
#     user='root',
#     passwd='123456',
#     db='test',
#     charset='utf8'
# )
#
# cursor=conn.cursor()
# sql_insert="insert into user(userid,username) values(10,'name10')"
# sql_update="update user set username='name91'where userid=9 "
# sql_delete="delete from user where userd<3"
# try:
#     cursor.execute(sql_insert)
#     print cursor.rowcount
#     cursor.execute(sql_update)
#     print cursor.rowcount
#     cursor.execute(sql_delete)
#     print cursor.rowcount
#     conn.commit()
# except Exception as e:
#     print e
#     conn.rollback()
#
#
# cursor.close()
# conn.close()




import MySQLdb
class bank_transform(object):
    def __init__(self,conn):
        self.conn=conn
    def trans_money(self,A,B,money):
        try:
            self.money_enough(A,money)
            self.check_id(A)
            self.check_id(B)
            self. reduce_A(A,money)
            self.add_B(B,money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e
    def money_enough(self,A,money):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where acctid=%s and money>=%s" %(A,money)
            cursor.execute(sql)
            rs=cursor.fetchall()
            if len(rs)!=1:
                raise Exception("账号%s没有足够的钱"%id)
        finally:
            cursor.close()

    def check_id(self,id):
        cursor = self.conn.cursor()
        try:
            sql="select * from account where acctid=%s "%id
            cursor.execute(sql)
            rs=cursor.fetchall()
            if len(rs)!=1:
                raise Exception("账号%s不存在"%id)
        finally:
            cursor.close()

    def reduce_A(self,A,money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money=money-%s where acctid=%s" %(money,A)
            cursor.execute(sql)
            rs = cursor.fetchall()
            if cursor.rowcount!= 1:
                raise Exception("账号%s减款失败" %A)
        finally:
            cursor.close()
    def add_B(self,B,money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money=money+%s where acctid=%s" %(money,B)
            cursor.execute(sql)
            rs = cursor.fetchall()
            if cursor.rowcount != 1:
                raise Exception("账号%s加款失败" %B)
        finally:
            cursor.close()


if  __name__=="__main__":
    A_trans=int(input("请输入转账用户："))
    B_trans=int(input("请输入获取转账用户："))
    money=int(input("请输入转账金额："))

    conn =MySQLdb.Connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='123456',
        db='test',
        charset='utf8'
    )
    result=bank_transform(conn)
    try:
        result.trans_money(A_trans,B_trans,money)
    except Exception as e:
        print "出现问题："+str(e)
    finally:
        conn.close()