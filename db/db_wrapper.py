#-*- coding: UTF-8 -*-

from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
# 表的名字:
    __tablename__ = 'user'

# 表的结构:
    id = Column(Integer, primary_key=True)
    priority = Column(Integer)
    name = Column(String(20))
    password = Column(String(128))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

if __name__ == "__main__":
# 创建session对象:
    session = DBSession()
    user = session.query(User).all()
    for one in user:
        print (one)
# 关闭session:
    session.close()
