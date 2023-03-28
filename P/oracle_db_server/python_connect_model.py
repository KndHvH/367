import cx_Oracle

# Conectar ao banco de dados Oracle
conn = cx_Oracle.connect('usuario/senha@endereco_do_servidor:porta/nome_do_banco')

# Criar um cursor para executar comandos SQL
cur = conn.cursor()

# Executar uma consulta SQL simples
cur.execute('SELECT * FROM tabela')

# Recuperar os resultados da consulta
rows = cur.fetchall()
for row in rows:
    print(row)

# Executar uma inserção no banco de dados
cur.execute("INSERT INTO tabela (coluna1, coluna2) VALUES ('valor1', 'valor2')")

# Executar uma atualização no banco de dados
cur.execute("UPDATE tabela SET coluna1 = 'novo_valor' WHERE id = 123")

# Finalizar o uso do cursor e da conexão com o banco de dados
cur.close()
conn.close()

