-- Active: 1669499925647@@127.0.0.1@3306@juicedb

# USE ~DB
CREATE TABLE
    tbClient(
        CPF VARCHAR(11),
        NAME VARCHAR(100),
        STREET VARCHAR(150),
        DISTRICT VARCHAR(50),
        CITY VARCHAR(50),
        STATE VARCHAR(50),
        CEP VARCHAR(8),
        BIRTHDAY DATE,
        AGE SMALLINT,
        GENDER ENUM('Masc', 'Femi'),
        CREDITLIMIT DOUBLE,
        MINBUY FLOAT,
        NEWCLIENT BIT(1)
    );

CREATE TABLE
    tbProducts(
        ID INT(10) ZEROFILL NOT NULL PRIMARY KEY,
        NAME VARCHAR(70),
        PACKAGE VARCHAR(30),
        SIZE VARCHAR(30),
        FLAVOUR VARCHAR(30),
        PRICE DOUBLE
    );

CREATE TABLE
    tbVendors(
        MATRICUL INT(6) ZEROFILL NOT NULL PRIMARY KEY,
        NAME VARCHAR(70),
        COMISSION DOUBLE
    );

INSERT INTO
    `tbProducts`(
        `ID`,
        `NAME`,
        `PACKAGE`,
        `SIZE`,
        `FLAVOUR`,
        `PRICE`
    )
VALUES (
        22349,
        'Frescor do Inverno - 2L - Pera',
        'PET',
        '2L',
        'Pera',
        12.99
    );

INSERT INTO
    `tbVendors`(
        `MATRICUL`,
        `NAME`,
        `COMISSION`
    )
VALUES (
        233,
        'Joao Geraldo da Fonseca',
        10
    );

DROP TABLE if EXISTS tbClient;

DROP TABLE if EXISTS tbProducts;