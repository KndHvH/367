from ftplib import *

ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())


login = input("Digite o Login: ")
password = input("Digite senha: ")

ftp.login(login,password)

print("Directory atual:",ftp.pwd())

ftp.cwd("pub")

print("Directory corrente:",ftp.pwd())

print(ftp.retrlines('LIST'))

ftp.quit()