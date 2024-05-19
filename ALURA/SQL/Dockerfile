# Use a imagem base do SQL Server
FROM mcr.microsoft.com/mssql/server:2019-latest

# Defina as variáveis de ambiente para a configuração do SQL Server
ENV ACCEPT_EULA=Y
ENV SA_PASSWORD=Minhasenha1234!

# Exponha a porta do SQL Server
EXPOSE 1433

# Inicie o SQL Server quando o contêiner for iniciado
CMD ["/opt/mssql/bin/sqlservr"]