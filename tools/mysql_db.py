import pymysql
from config.conf import MYSQL_INFO
import sys
from tools.logger import log
sys.path.append("..")

class Mysql_DB():
    """数据库连接"""
    def __init__(self):
        self.conn = pymysql.connect(
            host = MYSQL_INFO["hosts"],
            port = MYSQL_INFO["port"],
            user = MYSQL_INFO["username"],
            password = MYSQL_INFO["password"],
            db = MYSQL_INFO["db_name"]
        )
        self.cure = self.conn.cursor()

    # def __del__(self):
    #     self.cure.close()
    #     self.conn.close()

    def query(self,sql):
        log.info(sql)
        self.cure.execute(sql)
        return self.cure.fetchall()

    def exec(self,sql):
        try:
            log.debug(sql)
            self.cure.execute(sql)
            self.conn.commit()
        except Exception as e:
            log.info("回滚")
            self.conn.rollback()
            print(str(e))

    def check_user(self,sql):
        result = self.query(sql)
        return True if result else False


if __name__ == '__main__':
    sql = 'select * from user'
    aa= Mysql_DB().query(sql)
    print(aa)

