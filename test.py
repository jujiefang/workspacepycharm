import mysqlDB

def main():
    mysqldb = mysqlDB.MySqlDB()
    conn = mysqldb.getConnect()

if __name__ == '__main__':
    main()

