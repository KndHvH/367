import platform
import getpass
from datetime import datetime

print("Nome maquina",platform.node())
print("Arquitetura",platform.architecture())
print("Sistema operacional",platform.system())
print("Versao SO",platform.release())
print("Processador",platform.processor())
print("Python version",platform.python_version())

print(datetime.now())

print(getpass.getuser())
print(getpass.getpass("Digite sua senha"))

