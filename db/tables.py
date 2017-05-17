#-*- coding: UTF-8 -*-

import hashlib

from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from db_wrapper import  DBSession
# 创建对象的基类:
Base = declarative_base()

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

def query_user(line):
    session = DBSession()
    name, password = line.split('\3')
    sha512 = hashlib.sha512(password.encode()).hexdigest()
    result = session.query(User.priority).filter(User.name==name, User.password==sha512).one()
  
    session.close()
    return result[0] if len(result) else None

if __name__ == "__main__":
    line = 'root' + '\3' + '123'
    res = query_user(line)
    print(res)
