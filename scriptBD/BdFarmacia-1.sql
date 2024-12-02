create table cliente 
( 
idCliente serial primary key, 
nomeCliente varchar(60) not null, 
cpfCliente char(12), 
enderecoCliente varchar(80), 
celularCliente char(11), 
dataCadastro date 
); 

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

create table categoria
( 
idCategoria serial primary key, 
Descricao varchar(80), 
obs varchar(200) 
)

create table produto 
( 
idProduto serial primary key, 
idCategoria int references categoria(idCategoria),
nomeProduto varchar(60) not null, 
quantidade int null,
preco numeric(10,2) not null, 
tarja varchar(60) 
); 

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
