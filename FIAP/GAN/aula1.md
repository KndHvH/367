# Gan

Generative Adversarial Networks (GANs) são uma classe de modelos de aprendizado de máquina profundo que foram introduzidos pela primeira vez em 2014. Eles funcionam de maneira diferente de outros modelos de aprendizado de máquina, pois utilizam dois modelos diferentes, treinados juntos, para gerar novos dados. Um modelo, chamado "gerador", tenta gerar novos dados que sejam indistinguíveis de dados reais, enquanto o outro modelo, chamado "discriminador", tenta distinguir osdados gerados dos dados reais. O treinamento dos dois modelos é feito de forma adversarial, ou seja, o gerador tenta enganar o discriminador, e o discriminadortenta ser mais eficiente em detectar os dados gerados.

Já Advanced Nets são uma categoria mais ampla de redes neurais que incluem diferentes tipos de arquiteturas de rede neural, incluindo GANs, mas também outras redes neurais profundas, como redes neurais convolucionais (ConvNets), redes neurais recorrentes (RNNs) e outras. A ideia é que estes são modelos mais avançadose sofisticados, capazes de aprender representações mais complexas dos dados.



## Modelos generativos

Modelos generativos são modelos de aprendizado de máquina que são projetados para gerar novos dados que sejam similares a um conjunto de dados de treinamento. Em outras palavras, eles aprendem a distribuição subjacente dos dados e, em seguida, usam essa compreensão para gerar novos dados que sejam coerentes com o que foi visto nos dados de treinamento.

Existem vários tipos diferentes de modelos generativos, incluindo GANs, que foram mencionados anteriormente, bem como variational autoencoders (VAEs), que usam técnicas de codificação e decodificação para gerar novos dados. Outros modelos generativos incluem modelos baseados em árvores, modelos baseados em fluxo, e modelos baseados em Markov Chain Monte Carlo (MCMC).

Esses modelos são úteis em uma ampla gama de aplicações, incluindo a geração de imagens, a geração de texto, a geração de música e outros tipos de dados. Eles também podem ser usados para realizar tarefas de completude de dados, ou seja, preencher lacunas em conjuntos de dados incompletos.


## Modelos generativos estatisticos

Modelos generativos estatísticos são uma classe de modelos generativos que usam estatísticas para gerar novos dados. Esses modelos aprendem a distribuição de probabilidade dos dados de treinamento, o que significa que eles são capazes de gerar novos dados que sejam coerentes com a distribuição dos dados de treinamento.

Os modelos generativos estatísticos incluem a classificação Gaussiana Mixture Model (GMM), que representa a distribuição dos dados como uma mistura de várias distribuições Gaussianas. Outros exemplos incluem o Modelo de Mistura de Dirichlet (Dirichlet Mixture Model, DMM), o Modelo de Mistura de Hidden Markov (Hidden Markov Mixture Model, HMMM) e o Modelo de Mistura de Latent Dirichlet Allocation (Latent Dirichlet Allocation Mixture Model, LDA-MM).

Esses modelos são amplamente utilizados em uma ampla gama de aplicações, como a classificação de dados, a clusterização de dados, a geração de dados sintéticos e a detecção de anomalia. Eles também são úteis para explorar e visualizar dados complexos, já que podem ser usados para visualizar a distribuição subjacente dos dados.



## Modelos Generativos x Discriminativos

Modelos discriminativos e modelos generativos são duas abordagens diferentes para o aprendizado de máquina.

Modelos discriminativos são modelos que aprendem a discriminar entre diferentes classes ou categorias, dado um conjunto de entrada. Eles aprendem a separar as classes de uma maneira que melhor se ajuste aos dados de treinamento. Por exemplo, um modelo discriminativo pode ser treinado para classificar imagens como sendo de gatos ou cães.

Já modelos generativos, como mencionado anteriormente, são modelos que aprendem a gerar novos dados que sejam similares a um conjunto de dados de treinamento. Em vez de discriminar entre classes, eles aprendem a distribuição subjacente dos dados e usam essa compreensão para gerar novos dados coerentes.

Em resumo, modelos discriminativos aprendem a classificar dados, enquanto modelos generativos aprendem a gerar dados. Ambas as abordagens têm suas próprias vantagens e desvantagens e são usadas em diferentes contextos e aplicações.













