-- Active: 1715191248488@@127.0.0.1@1433@master


CREATE DATABASE suco_vendas


-- DROP DATABASE suco_vendas

use suco_vendas
CREATE TABLE cliente (
    cpf VARCHAR(11) PRIMARY KEY,
    nome_completo VARCHAR(100),
    rua VARCHAR(100),
    complemento VARCHAR(100),
    bairro VARCHAR(100),
    estado CHAR(2),
    cep CHAR(8),
    data_nascimento DATE,
    idade INT,
    sexo CHAR(1),
    limite_credito DECIMAL(10,2),
    volume_minimo_compra_produto DECIMAL(10,2),
    realizou_compra BIT
)


CREATE TABLE produto (
    codigo_produto INT PRIMARY KEY,
    nome_produto VARCHAR(100),
    embalagem VARCHAR(100),
    tamanho VARCHAR(100),
    sabor VARCHAR(100),
    preco_lista DECIMAL(10,2)
)