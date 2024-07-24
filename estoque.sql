create database estoque;
use estoque;
create table produtos(
codigo int primary key auto_increment,
nome varchar(100),
preco float,
estoque float);
insert into produtos values
(1, "Caneta", 3.50, 20),
(2, "Borracha", 5.90, 15),
(3, "Régua", 11.75, 40),
(4, "Pasta", 6.25, 10);