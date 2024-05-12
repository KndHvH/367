# Use a imagem oficial do Microsoft SQL Server
FROM mcr.microsoft.com/mssql/server:2019-latest

# Define as variáveis de ambiente necessárias
ENV ACCEPT_EULA=Y
ENV SA_PASSWORD=Minhasenha1234!
ENV MSSQL_PID=Express

# Expõe a porta padrão do SQL Server
EXPOSE 1433

# Executa o SQL Server
CMD ["/opt/mssql/bin/sqlservr"]