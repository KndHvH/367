-- Active: 1715545992131@@127.0.0.1@1433@ALURA

CREATE DATABASE ALURA

SELECT spid, status, loginame, DB_NAME(dbid) as dbname, cmd
FROM sys.sysprocesses
WHERE DB_NAME(dbid) = 'model'

KILL 53