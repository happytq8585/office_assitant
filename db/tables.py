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
    result = session.query(User).filter(User.name==name, User.password==sha512).all()
    for one in result:
        print(one.id, one.name, password)

    session.close()

if __name__ == "__main__":
    line = 'root' + '\3' + '123'
    query_user(line)
