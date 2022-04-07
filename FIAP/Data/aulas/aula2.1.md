# Cardinalidade

## Formato
(0,1) = (Minimo,Maximo)

---
##Exemplo
```
Funcionario -------------- Chefia -------------- Departamento
           (0,1)                                   (0,1)
```
- Um funcionario pode ser chefe de nenhum (0) ou de 1 departamento
- um departamento pode ser chefiado por nenhum ou por 1
---

```
Funcionario ------------- trabalha ------------- Departamento
            (1,n)                                   (1,1)
```
- Um funcionario pode trabalhar em um departamento no minimo e no maximo
- Em um departamento podem trabalhar 1 ou mais funcionarios
---

```
Funcionario ------------ Participa ------------- Projeto
            (1,n)                                   (1,n)
```

- Um funcionario pode participar de um ou mais projetos
- Um projeto pode ter um ou mais funcionariosg