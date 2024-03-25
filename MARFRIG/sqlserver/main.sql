
# docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=' -e "MSSQL_AGENT_ENABLED=true" -p 1433:1433 --name sqlserver -d mcr.microsoft.com/mssql/server:2019-latest

-- Active: 1711291963573@@127.0.0.1@1433@master
CREATE TABLE produto (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nome VARCHAR(100),
    descricao VARCHAR(255),
    preco DECIMAL(10, 2)
);


-- DELETE TABLE produto
DROP TABLE IF EXISTS produto;



INSERT INTO produto (nome, descricao, preco)
VALUES 
    ('Coca-Cola', 'Refrigerante Coca-Cola', 3.99),
    ('Pepsi', 'Refrigerante Pepsi', 2.99),
    ('Sprite', 'Refrigerante Sprite', 2.49),
    ('Guaraná Antarctica', 'Refrigerante Guaraná Antarctica', 3.49),
    ('Fanta Laranja', 'Refrigerante Fanta Laranja', 2.99),
    ('Fanta Uva', 'Refrigerante Fanta Uva', 2.99),
    ('Schweppes Citrus', 'Refrigerante Schweppes Citrus', 3.49),
    ('Kuat', 'Refrigerante Kuat', 2.49),
    ('Soda', 'Refrigerante Soda', 1.99),
    ('Água com Gás', 'Água com Gás', 1.49);   

    


CREATE PROCEDURE GetProdutoById @Id INT
AS
BEGIN
    SELECT * FROM produto WHERE id = @Id;
END;


CREATE PROCEDURE GetProdutosBelowPrice @Price DECIMAL(10, 2)
AS
BEGIN
    SELECT * FROM produto WHERE preco < @Price;
END;


CREATE PROCEDURE UpdateProdutoPrice @Id INT, @NewPrice DECIMAL(10, 2)
AS
BEGIN
    UPDATE produto SET preco = @NewPrice WHERE id = @Id;
END;



CREATE PROCEDURE InsertProduto @Nome VARCHAR(100), @Descricao VARCHAR(255), @Preco DECIMAL(10, 2)
AS
BEGIN
    INSERT INTO produto (nome, descricao, preco) VALUES (@Nome, @Descricao, @Preco);
END;

CREATE PROCEDURE IncreasePriceForLowCostProducts @ThresholdPrice DECIMAL(10, 2), @IncreasePercentage DECIMAL(5, 2)
AS
BEGIN
    -- Seleciona todos os produtos com preço abaixo do preço limite
    DECLARE @Id INT, @Price DECIMAL(10, 2);
    DECLARE LowCostProductsCursor CURSOR FOR
    SELECT id, preco FROM produto WHERE preco < @ThresholdPrice;

    -- Abre o cursor e busca a primeira linha
    OPEN LowCostProductsCursor;
    FETCH NEXT FROM LowCostProductsCursor INTO @Id, @Price;

    -- Loop através de todas as linhas
    WHILE @@FETCH_STATUS = 0
    BEGIN
        -- Calcula o novo preço
        DECLARE @NewPrice DECIMAL(10, 2);
        SET @NewPrice = @Price * (1 + @IncreasePercentage / 100);

        -- Chama a Stored Procedure para atualizar o preço
        EXEC UpdateProdutoPrice @Id, @NewPrice;

        -- Busca a próxima linha
        FETCH NEXT FROM LowCostProductsCursor INTO @Id, @Price;
    END;

    -- Fecha o cursor
    CLOSE LowCostProductsCursor;
    DEALLOCATE LowCostProductsCursor;
END;

CREATE PROCEDURE GetProdutosByName @Name VARCHAR(100)
AS
BEGIN
    SELECT * FROM produto WHERE nome LIKE '%' + @Name + '%';
END;


EXEC GetProdutoById 9;
EXEC GetProdutosBelowPrice 3.;
EXEC UpdateProdutoPrice 9, 2.49;
EXEC InsertProduto 'Água Tônica', 'Água Tônica Natural', 2.99;
EXEC IncreasePriceForLowCostProducts 3.00, 10.00;

EXEC GetProdutosByName 'Fanta';
SELECT * from produto;



EXEC sp_configure 'show advanced options', 1;
RECONFIGURE;
EXEC sp_configure 'Agent XPs', 1;
RECONFIGURE;




EXEC xp_servicecontrol N'querystate',N'SQLSERVERAGENT'

EXEC xp_servicecontrol N'start',N'SQLSERVERAGENT'


EXEC msdb.dbo.sp_add_job
    @job_name = N'IncreasePriceJob';


EXEC msdb.dbo.sp_add_jobstep
    @job_name = N'IncreasePriceJob',
    @step_name = N'IncreasePrice',
    @subsystem = N'TSQL',
    @command = N'EXEC IncreasePriceForLowCostProducts 100.00, 5.00;',
    @retry_attempts = 5,
    @retry_interval = 1;

EXEC msdb.dbo.sp_add_jobschedule
    @job_name = N'IncreasePriceJob',
    @name = N'EveryHalfHour',
    @freq_type = 4,
    @freq_interval = 1,
    @freq_subday_type = 4,
    @freq_subday_interval = 5,
    @freq_relative_interval = 0,
    @freq_recurrence_factor = 0,
    @active_start_date = 20220101,
    @active_start_time = 0;
    
    
EXEC msdb.dbo.sp_add_jobserver
    @job_name = N'IncreasePriceJob',
    @server_name = N'(local)';