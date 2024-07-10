create database vendas;
use vendas;
create table clientes(
id int primary key auto_increment,
nome varchar(100),
cidade varchar(100),
estado varchar(2),
saldo float);
insert into clientes values
(1, 'Camila', 'Mossoró',  'RN', 100),
(4, 'Josias', 'Natal',    'RN', 390),
(7, 'Aline',  'Fortaleza','CE', 0),
(12,'Marcio', 'Aracati',  'CE', 148),
(8, 'Pamela', 'Assu',     'RN', 0),
(2, 'Viviane','Beberibe', 'CE', 513);