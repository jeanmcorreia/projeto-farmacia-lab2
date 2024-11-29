create table cliente 
( 
idCliente serial primary key, 
nomeCliente varchar(60) not null, 
cpfCliente char(12), 
enderecoCliente varchar(80), 
celularCliente char(11), 
dataCadastro date 
); 
drop table funcionario 
create table funcionario 
( 
idFuncionario serial primary key, 
nomeFuncionario varchar(60) not null,
UsuarioFuncionario varchar(60) not null, 
cpfFuncionario char(12), 
enderecoFuncionario varchar(80), 
celularFuncionario char(11),
SenhaFuncionario varchar(60) not null,
NivelPermissao char(1) not null,
admissao date 
);


insert into categoria(Descricao, obs) values ('laticinios', 'derivados da vaca')
create table usuario
( 
Usuario varchar(80) unique not null, 
Password varchar(80) unique not null 
);




create table categoria
( 
idCategoria serial primary key, 
Descricao varchar(80), 
obs varchar(200) 
)


select * from tbl_detalhe_pedidos tdp 
create table produto 
( 
idProduto serial primary key, 
idCategoria int references categoria(idCategoria),
nomeProduto varchar(60) not null, 
preco numeric(10,2) not null, 
tarja varchar(60) 
); 
insert into produto (idcategoria , nomeproduto, preco, tarja) values (1, 'leite', 10, 'N/A')



create table pedido 
( 
idPedido serial primary key, 
idCliente int not null references cliente(idcliente), 
idFuncionario int not null references funcionario(idfuncionario), 
formaPagamento text not null, 
valorTotal numeric(10,2), 
dataPedido date
)


create table tbl_detalhe_pedidos(
	iddetalheP serial primary key,
	idPedido int not null references pedido(idPedido), 
	idProduto int not null references produto(idProduto),
	quantidade int not null
);


drop table detalhe_estoque 
create table detalhe_estoque (
idLote serial primary key,
idProduto int not null references produto(idProduto),
quantidade int not null,
validade date not null
)

select * from tbl_detalhe_pedidos tdp 
select * from pedido p
