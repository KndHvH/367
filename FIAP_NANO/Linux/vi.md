### 1 - vi
	vi arquivo.txt
cria o arquivo ou abre um existente

### 2 - q
	:q
	:q!
para sair ou sair sem salvar

### 3 - i
	i
para abrir insert / editar

### 4 - o 
	o
para abrir insert / editar na linha seguinte

### 5 - set nu
	:set nu
habilita numero nas linhas

### 6 - number
	:302
avanca para a linha de numero especifico

### 7 - w
	:w
salva documento sem sair

### 8 - x
	:wq
	:x
salvar e sair

### 9 - x,xw
	:3,5w arquivo.txt
cria um novo arquivo copiando as linhas de 3 a 5, com o nome especifico


### 10 - yy
	yy
	3yy
	p
copia x linhas e cola com p


### 11 - dd
	3dd
	dd
	p
apaga x linhas, p colar

### 12 - U
	U
Undo controlz


### 13 - /
	/
	enter
	n
	N
pesquis algo no doc, enter para ir para primeiro e n para proximo e N para anterior


### 14 - %s
	 %s/mais/menos/Gc
Substitui no formato antigo/novo/parametros, g - global, c - certeza	
