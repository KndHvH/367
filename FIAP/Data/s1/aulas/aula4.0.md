# SQLite

## Criando tabelas:
```
Microsoft Windows [Version 10.0.19042.1081]
(c) Microsoft Corporation. All rights reserved.

C:\Users\logonrmlocal>cd \

C:\>cd SQLite

C:\SQLite>sqlite3 alpha.db
SQLite version 3.38.2 2022-03-26 13:51:10
Enter ".help" for usage hints.
sqlite> CREATE TABLE programador (
   ...> idProgramador INTEGER PRIMARY KEY AUTOINCREMENT,
   ...> nome VARCHAR(50) NOT NULL,
   ...> cpf VARCHAR(11) NOT NULL,
   ...> habilidades VARCHAR(100)
   ...> )
   ...>

C:\SQLite>

```
## Listando tabelas:

```
sqlite> .tables
programador

sqlite> .schema programador
CREATE TABLE programador (
idProgramador INTEGER PRIMARY KEY AUTOINCREMENT,
nome VARCHAR(50) NOT NULL,
cpf VARCHAR(11) NOT NULL,
habilidades VARCHAR(100)
);
```

## Adicionando valores em tabelas:

```
sqlite> INSERT INTO programador (nome,cpf,habilidades)
   ...> VALUES ('Jose','12345678901','aws,sqlite,python');
   
sqlite> INSERT INTO programador (nome,cpf,habilidades)
   ...> VALUES ('Ana','48327449423','azure,c#,java,python');
```

## Consultando tabelas:

```
sqlite> SELECT * FROM programador;
1|Jose|12345678901|aws,sqlite,python
2|Ana|48327449423|azure,c#,java,python


sqlite> SELECT * FROM programador WHERE idProgramador=2;
2|Ana|48327449423|azure,c#,java,python


sqlite> SELECT * FROM programador ORDER BY nome;
2|Ana|48327449423|azure,c#,java,python
1|Jose|12345678901|aws,sqlite,python

sqlite> SELECT * FROM programador ORDER BY nome DESC;
1|Jose|12345678901|aws,sqlite,python
2|Ana|48327449423|azure,c#,java,python
```


## Alterando valores em tabelas:

```
sqlite> UPDATE programador
   ...> SET habilidades = 'aws,sqlite,python,azure'
   ...> WHERE idProgramador=1
   ...> ;
   
sqlite> UPDATE programador
   ...> SET habilidades = 'azure,c#,java,python,ibm cloud'
   ...> ,nome = 'Ana Silva'
   ...> WHERE idProgramador = 2;
```