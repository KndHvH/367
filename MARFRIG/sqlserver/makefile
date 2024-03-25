run-sqlserver:
	docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=Kndhvh1234' -e "MSSQL_AGENT_ENABLED=true" -p 1433:1433 --name sqlserver -d mcr.microsoft.com/mssql/server:2019-latest

stop-sqlserver:
	docker stop sqlserver

start-sqlserver:
	docker start sqlserver

restart-sqlserver:
	docker restart sqlserver

remove-sqlserver:
	docker rm sqlserver