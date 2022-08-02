# Cyber segurança

---
    
| Real / Predito | Sim                      | Não                      |
|----------------|--------------------------|--------------------------|
| Sim            | Verdadeiro Positivo (TP) | Falso Negativo  (FN)     |
| Não            | Falso Positivo (FP)      | Verdadeiro Negativo (TN) |

#### Verdadeiro Positivo (TP) 
- De fato um item **Proibido**  - (ex: pessoa tem HIV **Positivo**)


#### Verdadeiro Negativo (TN) 
- De fato um item **Permitido** - (ex: pessoa tem HIV **Negativo**)


####Falso Positivo (FP) 
- Nomeado como **Proibido** mas era **Permitido** - 
(ex: resultado de teste de HIV **Positivo** , mas a pessoa é saudavel)


#### Falso Negativo (FN)
- Nomeado como **Permitido** mas era **Negativo** -
(ex: resultado de teste de HIV **Negativo** , mas a pessoa esta doente)



##  Acuracia

###O que é
- é a quantidade de acertos do modelo dividido pelo total de amostras
-`(TP+TN)/(TP+TN+FP+FN)`

###Quando usar
- quando a amostra é balanceada e falsos positibos ou falsos negativos nao tem grande inpacto no negocio

## Precisão

### O que é
- de todos os dados classificados como positivos, quando sao realmente positivos
- `TP / (TP + FP)`

### Quando usar
- Quando precisamos garantir que ampliaremos os verdadeiros positivos. 
-  Uma precisao de 1.0 significa que nao houve nenhum falso positivo


## Recall

### O que é
- De todos os dados verdadeiros, quantos foram classificados verdadeiros
- `TP / (TP + FN)`

### Quando vai usar
- Quando precisamos garantir que nao teremos um falso negativo.
- Um recall de 1.0 significa que nao houve nenhum falso negativo.


## F1-Score
### O que é
- Essa métrica une precisao e recall a fim de trazer um numero unico que determine a qualidade geral do nosso modelo.
- `(Precisao * Recall) / (Precisao + Recall)`
  
### Quando usar
- Quando temos classes desbalanceadas e precisamos analisar os dados no geral.


