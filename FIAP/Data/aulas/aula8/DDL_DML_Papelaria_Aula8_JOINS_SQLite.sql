--Abrir o prompt de comando na pasta onde o SQLite está instalado
sqlite3 papelaria.db

-------------------------------
-- Tabela de clientes
-------------------------------
CREATE TABLE cliente (
  idCliente INTEGER PRIMARY KEY AUTOINCREMENT,
  nome varchar(100) NOT NULL,
  cidade varchar(50) NOT NULL
);

-------------------------------
--Dados de clientes
-------------------------------
INSERT INTO cliente VALUES (1,'Júlia','São Paulo'),(2,'Amanda','Belo Horizonte'),(3,'Roberto','Porto Alegre');

-------------------------------
--Tabela de fornecedores
-------------------------------

CREATE TABLE fornecedor (
  idFornecedor INTEGER PRIMARY KEY AUTOINCREMENT,
  nome varchar(50) NOT NULL,
  cidade varchar(50) NOT NULL
);

-------------------------------
--Dados de fornecedores
-------------------------------

INSERT INTO fornecedor VALUES (1,'Acme','São Paulo'),(2,'Northwind','Rio de Janeiro'),(3,'Atlas','Salvador');

-------------------------------
--Tabela de produtos
-------------------------------

CREATE TABLE produto (
  idProduto INTEGER PRIMARY KEY AUTOINCREMENT,
  dscProduto varchar(50) NOT NULL,
  valor decimal(10,2) NOT NULL,
  idFornecedor int NOT NULL,
  FOREIGN KEY (idFornecedor) REFERENCES fornecedor (idFornecedor)
);

-------------------------------
--Dados de produtos
-------------------------------

INSERT INTO produto VALUES (1,'Caderno',10.00,1),(2,'Lápis',5.00,1),(3,'Estojo',20.00,2),(4,'Borracha',10.00,2),(5,'Régua',15.00,3);

-------------------------------
--Tabela de pedidos
-------------------------------

CREATE TABLE pedido (
  idPedido INTEGER PRIMARY KEY AUTOINCREMENT,
  idCliente int NOT NULL,
  Data datetime NOT NULL,
  FOREIGN KEY (idCliente) REFERENCES cliente (idCliente)
);


-------------------------------
--Dados de pedidos
-------------------------------

INSERT INTO pedido VALUES (1,1,'2022-01-18 17:20:24'),(2,2,'2022-01-23 17:20:24'),(3,1,'2022-01-28 17:20:24'),(4,2,'2022-02-01 17:20:24');


-------------------------------
--Tabela de itens pedidos
-------------------------------

CREATE TABLE itempedido (
  idItemPedido INTEGER PRIMARY KEY AUTOINCREMENT,
  idPedido int NOT NULL,
  idProduto int NOT NULL,
  quantidade int NOT NULL,
  valorUnitario decimal(10,2) NOT NULL,
  FOREIGN KEY (idPedido) REFERENCES pedido (idPedido),
  FOREIGN KEY (idProduto) REFERENCES produto (idProduto)
); 

-----------------------------------
--Dados de itens pedidos
-----------------------------------

INSERT INTO itempedido VALUES (1,1,1,1,10.00),(2,1,2,2,5.00),(3,2,3,1,20.00),(4,3,4,2,10.00),(5,4,1,1,10.00),(6,4,2,1,5.00);


