## Tipos
Erros de OUT OF RANGE, vao ocorrer quando os limites forem estourados

#### Int

- 4 bytes
- ~2 Trilhões de dados
- ~4 Trilhões de dados com Unsigned (sem sinal de + ou -)
- Variacoes: TinyInt, SmallInt, MediumInt e BigInt
  
#### Float

- Float: 4 Bytes
- Double: 8 Bytes

Exemplo:

FLOAT(7,4)

999,00009  ->  999,0001

#### Numeric
- Até 65 Digitos
- Especificamos numero de casas decimais e digitos

Exemplo:

DECIMAL(5,2)

-999,99 <-> 999,99


#### Bit
- Até 64 bits
- Booleano


Exemplo:

BIT(1) -> 0 , 1
BIT(2) -> 00 , 01 , 10 , 11


#### Date

- DATE - 1000-01-01 <-> 9999-12-31
- DATETIME - 1000-01-01 00:00:00 <-> 9999-12-31 23:59:59
- TIMESTAMP - 1970- 01-01 00:00:01 UTC <-> 2038-01-19 23:59:59 UTC
- TIME - -838:59:59 <-> 838:59:59
- YEAR - 1901 <-> 2155 (2 ou 4 Digitos)

#### Atributos:

- SIGNED ou UNSIGNED:
  - Possui ou nao sinal numérico (+,-)

- ZEROFILL:
  - Preenche com 0 os espaços vazios
  - Exemplo: INT(4)
  - 5  ->  0005

- AUTO_INCREMENT:
  - Sequencia auto incrementada
  - 0,1,2,3,4...



##### Strings

- CHAR(4) - 'aa' -> '__aa' 
- VARCHAR(4) - 'aa' -> 'aa'
- ENUM:
  - Permite armazenar uma lista pré definida de valores
  - ex: ENUM('x-small','small','medium','large','x-large')
 



