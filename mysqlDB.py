import pymysql
print("我是连接数据库的代码")
class MySqlDB():
    def __init__(self):
        self.getConnect()

    def getConnect(self):
        self.conn = pymysql.connect(host='localhost', user='root', password="root",
                 database='python', port=3306)
        print(self.conn)
        return self.conn

def main():
    mysqldb = MySqlDB()

if __name__ == '__main__':
    main()




