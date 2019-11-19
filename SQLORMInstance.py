from sqlalchemy import create_engine,Column,Integer,String,DateTime,Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
#此处若抛出“No module named 'MySQLdb"的异常，请安装MySQLdb模块或mysqlClient模块
engine = create_engine("mysql://root:root@localhost:3306/news?charset=utf8")
class News(Base):
        __tablename__ ='news'
        id = Column(Integer, primary_key=True,)
        title = Column(String(100),nullable=False)
        content = Column(String(2000), nullable=False)
        type = Column(String(10), nullable=False)
        image = Column(String(300), nullable=True)
        author = Column(String(50), nullable=True)
        view_count =  Column(Integer, nullable=True,default=0)
        create_date = Column(DateTime, nullable=True)
        is_valid = Column(Boolean, nullable=True,default=True)



