-- Active: 1669499925647@@127.0.0.1@3306@juicedb

UPDATE `tbProducts`
SET
    `PACKAGE` = 'Lata',
    `PRICE` = 2.46
WHERE `ID` = 544931;

DELETE FROM `tbProducts` WHERE `ID` = 544931;

ALTER TABLE `tbProducts` ADD PRIMARY KEY (ID);

ALTER TABLE `tbProducts` ADD COLUMN  (CREATED TIME);


ALTER TABLE `tbProducts` MODIFY CREATED DATE;

SELECT * FROM `tbProducts`;

UPDATE `tbProducts`
SET
    `CREATED` = '2022-12-02';

UPDATE `tbProducts`
SET
    `FLAVOUR` = 'Melancia'
WHERE `FLAVOUR` = 'Melância'