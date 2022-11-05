### 1 - man
    man sudo
retorna o manual do comando sudo. usar / para pesquisar

### 2 - su
    su
troca de usuario, se nao for completado ira para o root

### 3 - passwd
    passwd root
troca a senha do usuario ou de um especifico

### 4 - adduser
    sudo adduser usuariotest
cria novo usuario, precisa do sudo e de um nome

### 5 - groupadd
    sudo groupadd grupo
cria novo grupo, precisa do sudo e de um nome

### 6 - usermod
    sudo usermod -aG grupo usuariotest
modifica usuario, permitindo adicionar grupos etc

### 7 - ls
    ls /
abre o dir 

### 8 - pwd
    pwd
mostra dir atual

### 9 - mkdir
    mkdir novapasta
cria novo dir

### 10 - cp
    cp arquivo.txt /tmp arquivo2.txt
    cp -rpv Downloads/ Downloads2/
copia arquivo ou dir

### 11 - mv
    mv Arquivo.txt NovoArquivo.txt
    mv Downloads/ /temp 
mover ou renomear arquivo

### 12 - rmdir
    rmdir dir
apaga um dir

### 13 - rm
    rm Arquivo.txt
apagar arquivos

### 14 - tail
    sudo tail -n 7 /var/log/syslog
head para ver x n de linhas de um arquivo e tail para ultimas

### 15 - less
    sudo less /var/log/syslog
abre o doc no terminal

### 16 - locate
    locate sprint4.py
procura um arquivo pelo nome

### 17 - grab
    grep pulseaudio /var/log -r 
procura ocorrencia de palabra chave em arquivos

### 18 - links
    links google.com
abre o navegador pelo terminal

### 19 - tar
    tar -czvf file.tar.gz *.py
    tar -xzvf file.tar.gz 
junta arquivos da pasta e comprime com gz
c - compress
z - utiliza gzip
v - verbose
f - name
x - descompress

### 20 - top
    top
abre gerenciador de tarefas no terminal

### 21 - kill
    kill 53301
mata o processo pelo pid    

### 22 - fdisk
	sudo fdisk /dev/sda
abre prompt dos discos

### 23 - nautilus
	nautilus --browser
abre o file explorer

