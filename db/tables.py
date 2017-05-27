#-*- coding: utf-8 -*-

import hashlib

from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from db_wrapper import  DBSession

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# 创建对象的基类:
Base = declarative_base()

class Agency(Base):
    __tablename__ = 'agency'
    #机构的id: 在插入时候自动生成
    id = Column(Integer, primary_key=True)
    #机构名称: 工商银行 农业银行 招商银行 浦发银行…
    name = Column(String(128))

class Branch(Base):
    __tablename__ = 'branch'
    #分支机构的id: 在插入时候自动生成
    id = Column(Integer, primary_key=True)
    #机构的id: 工商银行id  农业银行id …
    agency_id = Column(Integer)
    #分支机构的地址
    address   = Column(String(128))
    #分支机构的电话
    telephone = Column(String(16))
    #分支机构的权限
    priority  = Column(Integer)
    #分支机构的名称
    name = Column(String(128))

class User(Base):
# 表的名字:
    __tablename__ = 'user'

# 表的结构:
    #用户的id
    id = Column(Integer, primary_key=True)
    #用户的权限
    priority = Column(Integer)
    #用户的名字
    name = Column(String(20))
    #用户的密码hash值
    password = Column(String(128))
    #用户所在分支机构的id
    branch_id = Column(Integer)
    #用户的电话
    telephone = Column(String(16))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/test',encoding='utf-8')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

#失败返回None
#成功返回[priority, [branch], [agency]]
def query_user(line):
    session = DBSession()
    name, password = line.split('\3')
    sha512 = hashlib.sha512(password.encode()).hexdigest()
    res = session.query(User.priority, User.branch_id).filter(User.name==name, User.password==sha512).first()
    if not res:
        return None
    
    priority = res.priority
    branch_id = res.branch_id
    res = session.query(Branch).filter(Branch.id == branch_id).first()
    if not res:
        return None
    branch = [res.id, res.agency_id, res.address, res.telephone, res.priority, res.name]
    res = session.query(Agency).filter(Agency.id == branch[1]).first()
    if not res:
        return None
    session.close()
    agency = [res.id, res.name]
    return [priority, branch, agency]
if __name__ == "__main__":
    line = 'root' + '\3' + '123'
    res = query_user(line)
    print(res[0])
    for e in res[1]:
        print(e)
    for e in res[2]:
        print(e)
