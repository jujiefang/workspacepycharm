import  MySQLdb
conn = MySQLdb.connect('localhost','root','root','python',3306)
print(conn)
#获取游标

cursor = conn.cursor()

#删除 一张表
dropSQL = "drop table  if  exists ss"
cursor.execute(dropSQL)
conn.commit()

#删除表中的数据
# deleteSQL = "delete from ss where id = %s"
# cursor.execute(deleteSQL,(6,))
# conn.commit()


#修改表中记录
# updateSql = "update ss set name = %s where id =%s"
# value = ('lililili',3)
# cursor.execute(updateSql,value)
# conn.commit()


#查询多条语句
# selectOneSql = "select * from ss where name = %s"
# cursor.execute(selectOneSql,('tt',))# 此处 必须写元组
# result = cursor.fetchall()
# for row in result:
#     print(row[0],"-----",row[1])
# print(result)
# conn.close()


#查询一条语句
# selectOneSql = "select * from ss where id =%s "
# cursor.execute(selectOneSql,(5,))#此处必须写元组
# #dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；
# # 带参数时，返回参数的属性、方法列表
# print(dir(cursor))
# result = cursor.fetchone()
# print(cursor.description)#得到域的名字
#
# print(result[0])#不能直接的看到是取的哪个属性，可使用dict()进行转换 dict() 函数用于创建一个字典。
#
# #每次取出一个元素放到k中，只取k的第一个元素  与数据进行打包
# r = zip([k[0] for k in cursor.description],result)
# print(type(r)) #<class 'zip'>
# for i in r:
#     print(i)  #('id', 5) ('name', 'tt')
# #将数据转为字典
# ru = dict(zip([k[0] for k in cursor.description],result))
# print(ru)
# print(ru['id'])




# #插入一条语句，
# insertSql ="insert into ss(name) values(%s)"
# cursor.execute(insertSql,[('tt1')])
# #执行完成后需要 提交 事务
# conn.commit()


#插入一条语句， 字符串拼接
# insertSql ="insert into ss(name) values('%s')"%('tt')
# cursor.execute(insertSql)
# #执行完成后需要 提交 事务
# conn.commit()

# #同时插入多条语句
# insertSql ="insert into ss(name) values(%s)"
# data = [('zhansan'),('liuliu'),('qiqi')]
# cursor.executemany(insertSql,data)
# #执行完成后需要 提交 事务
# conn.commit()


# #插入语句
# insertSql ="insert into ss(name) values('lisi')"
# cursor.execute(insertSql)
# #执行完成后需要 提交 事务
# conn.commit()


# #获取游标
# cursor = conn.cursor()
# print(cursor)
# #建表sql语句
# sql = "create table ss(id int primary key  auto_increment,name varchar(20))"
# #执行sql语句
# cursor.execute(sql)