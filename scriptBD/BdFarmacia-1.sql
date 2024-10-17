create table cliente 
( 
idCliente serial primary key, 
nomeCliente varchar(60) not null, 
cpfCliente char(12), 
enderecoCliente varchar(80), 
celularCliente char(11), 
dataCadastro date 
); 
select * from cliente
select * from tbl_detalhe_pedidos tdp 
select * from pedido
select * from funcionario 
select * from detalhe_estoque 
select * from produto 

create table funcionario 
( 
idFuncionario serial primary key, 
nomeFuncionario varchar(60) not null, 
cpfFuncionario char(12), 
enderecoFuncionario varchar(80), 
celularFuncionario char(11), 
admissao date 
);
SELECT * FROM funcionario

drop table usuario 
create table usuario
( 
Usuario varchar(80) unique not null, 
Password varchar(80) unique not null 
);

SELECT usuario, password from usuario

drop table categoria cascade
create table categoria
( 
idCategoria serial primary key, 
Descricao varchar(80), 
obs varchar(200) 
)
select * from produto p 


create table produto 
( 
idProduto serial primary key, 
idCategoria int references categoria(idCategoria),
nomeProduto varchar(60) not null, 
preco numeric(10,2) not null, 
tarja varchar(60) 
); 
drop table produto cascade

drop table pedido cascade
create table pedido 
( 
idPedido serial primary key, 
idCliente int not null references cliente(idcliente), 
idFuncionario int not null references funcionario(idfuncionario), 
formaPagamento text not null, 
valorTotal numeric(10,2), 
dataPedido date
)

drop table tbl_detalhe_pedidos 
create table tbl_detalhe_pedidos(
	iddetalheP serial primary key,
	idPedido int not null references pedido(idPedido), 
	idProduto int not null references produto(idProduto),
	quantidade int not null
);
select * from produto 
select * from detalhe_estoque
select * from tbl_detalhe_pedidos 
select * from pedido 
SELECT * FROM cliente 
SELECT * from funcionario 

drop table detalhe_estoque
create table detalhe_estoque (
idLote int,
idProduto int not null references produto(idProduto),
quantidade int not null,
validade date not null
)
select * from detalhe_estoque
select * from usuario
