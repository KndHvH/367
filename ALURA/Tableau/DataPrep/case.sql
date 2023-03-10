CASE [Nome Colunas]
WHEN 1 THEN IF ISNULL([Country]) THEN 'Com valor' ELSE 'Sem valor' END
WHEN 2 THEN IF ISNULL([Region]) THEN 'Com valor' ELSE 'Sem valor' END
WHEN 3 THEN IF ISNULL([Economy (GDP per Capita)]) THEN 'Com valor' ELSE 'Sem valor' END
WHEN 4 THEN IF ISNULL([Family]) THEN 'Com valor' ELSE 'Sem valor' END
WHEN 5 THEN IF ISNULL([Freedom]) THEN 'Com valor' ELSE 'Sem valor' END
WHEN 6 THEN IF ISNULL([Happiness Rank]) THEN 'Com valor' ELSE 'Sem valor' END
WHEN 7 THEN IF ISNULL([Happiness Score]) THEN 'Com valor' ELSE 'Sem valor' END
END


IF 'value'
THEN 'Com valor'
ELSE 'Sem valor'
END

END














IF [Tipo] = "Receita"
THEN [Crédito] - [Débito]
ELSE [Débito] - [Crédito]
END