create table if not exists agency
(
 id int(4) not null primary key auto_increment,
 name varchar(128) not null
) engine=InnoDB default charset=utf8;
insert into agency(name) values('人民银行成都分行'), ('招商银行');

create table if not exists branch
(
 id int(4) not null primary key auto_increment,
 agency_id int(4) not null,
 address varchar(128) not null,
 telephone varchar(16) not null,
 priority int(4) not null,
 name varchar(128) not null
) engine=InnoDB default charset=utf8;
insert into branch(agency_id, address, telephone, priority, name) values(1, '成都倪家桥', '123456', 100, '人民银行成都分行'), (2, '成都桐梓林', '999999', 10, '招商银行成都分行');

create table if not exists user 
(
 id int(4) not null primary key auto_increment,
 priority int(4) not null default 1,
 name varchar(20) not null,
 password varchar(128) not null,
 branch_id int(4) not null,
 telephone varchar(16)
 ) engine=InnoDB default charset=utf8;

insert into user(priority, name, password, branch_id, telephone) values(100, 'root', '3c9909afec25354d551dae21590bb26e38d53f2173b8d3dc3eee4c047e7ab1c1eb8b85103e3be7ba613b31bb5c9c36214dc9f14a42fd7a2fdb84856bca5c44c2', 1, '136-123456');
insert into user(name, password, branch_id, telephone) values('admin', '3c9909afec25354d551dae21590bb26e38d53f2173b8d3dc3eee4c047e7ab1c1eb8b85103e3be7ba613b31bb5c9c36214dc9f14a42fd7a2fdb84856bca5c44c2', 2, '136-999999');
