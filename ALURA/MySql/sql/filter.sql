-- Active: 1669499925647@@127.0.0.1@3306@juicedb
SELECT * FROM `tbProducts` WHERE `FLAVOUR` = 'Uva';

SELECT * FROM `tbProducts` WHERE `FLAVOUR` = 'Melancia';

SELECT * FROM `tbClient` WHERE AGE > 18 AND `GENDER` = 'Femi';

SELECT * FROM `tbClient` WHERE `STATE` <> 'SP';

SELECT * FROM `tbClient` WHERE `NAME` > 'g';

SELECT * FROM `tbProducts` WHERE `PRICE` = 10.512;

SELECT * FROM `tbClient` WHERE `BIRTHDAY` > '1995-01-13';

SELECT * FROM `tbClient` WHERE YEAR(`BIRTHDAY`) >= '1995';

SELECT * FROM `tbClient` WHERE MONTH(`BIRTHDAY`) = '10';

SELECT * FROM `tbClient` WHERE `AGE` = 18 or `AGE` = 22;