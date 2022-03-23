# Cyber segurança

---
    
|Real / Predito| Sim |Não |
    |--- |--- |--- |
    | Sim | Verdadeiro Positivo (TP) | Falso Negativo  (FN) |
    | Não | Falso Positivo (FP)| Verdadeiro Negativo (TN)|


##  Acuracia

###O que é
- é a quantidade de acertos do modelo dividido pelo total de amostras


###Quando usar
- quando a amostra é balanceada e falsos positibos ou falsos negativos nao tem grande inpacto no negocio

## Precisão

### O que é
- de todos os dados classificados como positivos, quando sao realmente positivos

### Quando usar
- Quando precisamos garantir que ampliaremos os verdadeiros positivos. 
-  Uma precisao de 1.0 significa que nao houve nenhum falso positivo


## Recall

### O que é
- De todos os dados verdadeiros, quantos foram classificados verdadeiros

### Quando vai usar
- Quando precisamos garantir que nao teremos um falso negativo.
- Um recall de 1.0 significa que nao houve nenhum falso negativo.


## F1-Score
### O que é
- Essa métrica une precisao e recall a fim de trazer um numero unico que determine a qualidade geral do nosso modelo.
- Quando temos classes desbalanceadas e precisamos analisar os dados no geral.


