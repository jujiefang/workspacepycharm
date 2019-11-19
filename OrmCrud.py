from SQLORMInstance import News
from sqlalchemy.orm import sessionmaker   #导入包
from SQLORMInstance import engine
Session = sessionmaker(bind=engine) #sessionmaker方法创建了一个Session工厂。
class OrmCRUD():
    def __init__(self):
        self.session = Session()#sessionmaker方法创建了一个Session工厂
    #删除数据
    def delete_data(self,id):
        #先查询
        news = self.session.query(News).get(id)
        #再删除
        self.session.delete(news)
        self.session.commit()
        return news
    #修改数据
    # def update_data(self,id):
    #     #先查询
    #     news = self.session.query(News).get(id)
    #     #再修改
    #     news.is_valid = 0
    #     self.session.add(news)
    #     self.session.commit()
    #     return news
    #模糊查询
    # def get_more_like(self,title):
    #     return self.session.query(News).filter(News.title.like(title))

    #过滤查询
    # def get_more2(self):
    #     return self.session.query(News.id,News.title).filter_by(is_valid=0)
    # #查询多条记录
    # def get_more(self):
    #     return self.session.query(News,News.title).filter_by(is_valid=0,title='人工智能')#多个条件 ,号隔开


    #查询所有的记录
    # def get_all(self):
    #     return self.session.query(News).all()
    # #查询一条记录 根据id查询一条记录信息
    # def get_one(self,id):
    #     return self.session.query(News).get(id)

    #查询多条记录
    # def addDate(self):
    #     new_object = News(title='人工智能22',content='人工时代已经到来了',type='科技')
    #     self.session.add(new_object)
    #     self.session.commit()
    # #添加多条记录
    # def addMoreDate(self):
    #     newObjects = [News(title='人工智能33',content='人工时代已经到来了',type='科技'),
    #                   News(title='人工智能44',content='人工时代已经到来了',type='科技'),
    #                   News(title='人工智能55',content='人工时代已经到来了',type='科技')]
    #     self.session.add_all(newObjects)
    #     self.session.commit()
#测试删除数据
ormCrud = OrmCRUD()
result = ormCrud.delete_data(11)
print(result)
#测试更新数据
# ormCrud = OrmCRUD()
# result = ormCrud.update_data(11)
# print(result.is_valid)
#测试模糊查询
# ormCrud = OrmCRUD()
# result = ormCrud.get_more_like('%人%')
# for item in result:
#     print("id:{0}--->title:{1}".format(item.id, item.title))
#测试过滤查询
# ormCrud = OrmCRUD()
# result = ormCrud.get_more2()
# for id,title in result:
#     print("id:{0}--->title:{1}".format(id,title))



#测试查询多个记录
# ormCrud = OrmCRUD()
# result = ormCrud.get_more()
# for item,title in result:
#       print(type(item))
#       print(item.title,title)

#测试添加多条记录
# ormCrud = OrmCRUD()
# result = ormCrud.addMoreDate()
# print(result) #返回None
#测试查询所有
# ormCrud = OrmCRUD()
# result = ormCrud.get_all()
# for item in result:
#     print(item.title)

#测试查询一条记录
# ormCrud = OrmCRUD()
# result = ormCrud.get_one(6)
# print("id:{0}--->title:{1}".format(result.id,result.title))


#测试添加数据
# ormCrud = OrmCRUD()
# ormCrud.addDate()