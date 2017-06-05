/*用户表user:
id: 用户的id,数据库中标识所用,自动递增  not null
nick_name: 用户的昵称                   not null
real_name: 用户的真是名字               not null
email:     用户的邮箱                   
branch:    用户所在金融机构或商业银行分支结构
telephone: 用户的电话
 */
/*用户表user*/
create table if not exists user
(
 id int unsigned  primary key auto_increment,
 nick_name varchar(128) not null,
 real_name varchar(128) not null,
 email varchar(256) default "",
 branch varchar(256) default "",
 telephone varchar(16) default ""
) engine=InnoDB default charset=utf8;
insert into user(nick_name, real_name, telephone) values("root", "root", "17313615918");/*id=1*/
<!--insert into user(nick_name, real_name, telephone) values("bank", "CommerceBank", "18600000001");/*id=2*/>

/*
权限:authority
id: 权限的id, 供数据库标识所用
code: 区域码, 用以限制该权限的地域区间, 一个int(4)整数表示
其中: 省   市   县(区)    id
      00   00   00    000
省、市、县(区)均用两位十进制表达, 县以内的所有银行用三位十进制表达
      四川省  10
             成都市  01
                    青羊区    001
                    锦江区    002
                    金牛区    003
                    武侯区    004
                    成华区    005
                    龙泉驿区  006
                    青白江区  007
                    新都区    008
                    温江区    009
                    双流县    010
                    郫县      011
                    金堂县    012
                    大邑县    013
                    蒲江县    014
                    新津县    015
                    都江堰市  016
                    崇州市    017
                    邛崃市    018
                    彭州市    019
                 
name: 操作动作名称, 创建用户的权限包括所有权限
查询数据 录入数据 修改数据 检测数据 创建用户
   1        2        3        4        5
value: 该动作名称对应的数字
*/
/*
权限:authority
*/
create table if not exists authority
(
 id int unsigned primary key auto_increment,
 code int unsigned not null,
 area varchar(128) not null,
 name varchar(32) not null,
 value int(4) not null
) engine=InnoDB, charset=utf8;
insert into authority(code, area, name, value) values(1001000, "四川省成都市", "创建用户", 5);
/*
insert into authority(code, area, name, value) values(1001001, "四川省成都市青羊区", "创建用户", 5);
insert into authority(code, area, name, value) values(1001004, "四川省成都市武侯区", "查询数据", 1);
insert into authority(code, area, name, value) values(1001004, "四川省成都市武侯区", "录入数据", 2);
insert into authority(code, area, name, value) values(1001004, "四川省成都市武侯区", "修改数据", 3);
insert into authority(code, area, name, value) values(1001006, "四川省成都市龙泉驿区", "创建用户", 5);
insert into authority(code, area, name, value) values(1001009, "四川省成都市双流县", "创建用户", 5);

insert into authority(code, area, name, value) values(1001011, "四川省成都市郫县", "查询数据", 1);
insert into authority(code, area, name, value) values(1001011, "四川省成都市郫县", "录入数据", 2);
insert into authority(code, area, name, value) values(1001011, "四川省成都市郫县", "修改数据", 3);
*/
/*
   角色: role
id: 数据库中用以表示条目所用, 自增
name: 角色名字
value: 角色对应的数字
*/
/*
角色: 系统管理员 货金部主要负责人 货金部分管负责人 业务管理人员 商业银行工作人员
         1            2                3               4            5
*/
create table if not exists role
(
 id int unsigned primary key auto_increment,
 name varchar(32) not null,
 value int unsigned not null
) engine=InnoDB, charset=utf8;
insert into role(name, value) values("系统管理员", 1);
insert into role(name, value) values("货金部主要负责人", 2);
insert into role(name, value) values("货金部分管负责人", 3);
insert into role(name, value) values("业务管理人员", 4);
insert into role(name, value) values("商业银行工作人员", 5);
/*
   用户权限表:user_authority
id: 数据库中标识条目，自动递增
userid: 用户的id
authid: 权限的id
*/
/*
   用户权限表:user_authority
*/
create table if not exists user_authority
(
 id int unsigned primary key auto_increment,
 userid int unsigned not null,
 authid int unsigned not null
) engine=InnoDB, charset=utf8;
insert into user_authority(userid, authid) values(1, 1);
/*
   用户角色表:user_role
id: 数据库中标识条目，自动递增
userid: 用户的id
roleid: 权限的id
*/
create table if not exists user_role
(
 id int unsigned primary key auto_increment,
 userid int unsigned not null,
 roleid int unsigned not null
) engine=InnoDB, charset=utf8;
insert into user_role(userid, roleid) values(1, 1);
