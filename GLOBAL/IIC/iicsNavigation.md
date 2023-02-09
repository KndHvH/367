


# IICS x PowerCente

PowerCenter is a client server based product X IICS is a native cloud offer 

Just need a browser to use IICS!



## Login

In IICS, each login is assosiated to an org, and an org is an equivalent of a powercenter repo


## Administrator Service

- New repo
- Select user, groups and roles


## Data Integration Service

- Dashboard with overview of enviroement
- Maping
- Sections
- WorkFlows

### Explore

- Projects in org

#### Project

- see Foulder in it
- add Foulder
- remove Foulder

##### Foulder

- see assets


### New

- Create Mapping
- Mapping templates
- Create TaskFlow
- TaskFlow templates 


#### Creating a new Mapping

- Mapping canvas
- Transformations options
- New Mapping task


### My Jobs

- See Status of anything schedule 


## Monitor Service

- Status of anything running





# Glossario

### O que é Power Center

PowerCenter é uma plataforma de integração de dados desenvolvida pela Informatica. É utilizado por empresas para integrar, gerenciar e compartilhar dados em vários sistemas, aplicativos e fontes de dados, incluindo bancos de dados relacionais, arquivos, sistemas cloud e muito mais.

Com o PowerCenter, os dados podem ser capturados, limpados, transformados e carregados em uma única fonte centralizada, permitindo que as empresas obtenham umavisão única e consistente dos dados em sua organização. Isso ajuda a melhorar a tomada de decisão e a eficiência dos processos empresariais. Além disso, o PowerCenter oferece ferramentas avançadas de monitoramento e gerenciamento de desempenho para garantir a qualidade e a integridade dos dados integrados.

### O que é IICS?

Informatica Intelligent Cloud Services (IICS) é uma plataforma de integração de dados baseada em nuvem desenvolvida pela Informatica. Ele permite que as empresas integrem, gerenciem e compartilhem dados em vários sistemas, aplicativos e fontes de dados, incluindo bancos de dados, aplicativos SaaS, nuvens públicas e privadas e muito mais.

Com o IICS, as empresas podem automatizar processos de integração de dados em larga escala, aproveitando a flexibilidade, escalabilidade e segurança da nuvem. Além disso, o IICS oferece uma ampla gama de ferramentas de integração, incluindo integração de aplicativos, integração de dados, gerenciamento de metadados, análise de dados e inteligência artificial. Isso ajuda as empresas a obter uma visão única e consistente dos dados em sua organização, melhorando a tomada de decisão e a eficiência dos processos empresariais.


### O que é um Mapping no IICS?

Em Informatica Intelligent Cloud Services (IICS), um mapping é um diagrama que representa a transformação de dados de uma fonte para uma destinação. Ele é usado para definir as regras de transformação e as relações entre os campos de dados.

Um mapping pode incluir várias etapas, como filtragem de dados, conversão de tipos de dados, agregação de dados, junção de dados e muito mais. Cada uma dessas etapas é representada por um objeto gráfico no mapping, que pode ser configurado e personalizado para atender às necessidades específicas de cada projeto.

Os mappings são usados para integrar dados de diferentes fontes e destinações, e são uma parte importante do processo de integração de dados no IICS. Eles permitem que as empresas automatizem e otimizem a integração de dados, ajudando a melhorar a qualidade e a consistência dos dados em sua organização.


### Um Mapping pode ser considerado um Pipeline?

Sim, um mapping no Informatica Intelligent Cloud Services (IICS) pode ser considerado como um pipeline de processamento de dados. Um pipeline é uma seqüência de etapas que são executadas em série para transformar dados de uma fonte para uma destinação. Em um pipeline de processamento de dados, cada etapa realiza uma tarefa específica, como filtrar dados, converter tipos de dados, agregar dados, junção de dados, entre outras.

O mapping no IICS é uma representação gráfica do pipeline de processamento de dados, onde cada etapa é representada por um objeto gráfico e as relações entre as etapas são representadas por conexões entre os objetos. O mapping permite que você configure e personalize as etapas para atender às suas necessidades específicas.

Portanto, um mapping no IICS pode ser considerado como um pipeline de processamento de dados, pois representa a seqüência de etapas que são executadas para transformar dados de uma fonte para uma destinação.


### O que é Mapping Task?

Em Informatica Intelligent Cloud Services (IICS), um Mapping Task é uma tarefa que representa uma etapa de transformação de dados em um pipeline de processamento de dados. Ele é usado para transformar dados de uma fonte para uma destinação específica, como um banco de dados ou um arquivo.

Um Mapping Task é baseado em um mapping, que é uma representação gráfica das regras de transformação e das relações entre os campos de dados. O Mapping Task executa as regras de transformação definidas no mapping para transformar os dados de entrada em dados de saída.

Os Mapping Tasks são executados em um ambiente de processamento de dados, que é responsável por ler os dados de entrada, executar as regras de transformação e escrever os dados de saída. Eles são uma parte importante do processo de integração de dados no IICS, pois permitem que as empresas automatizem e otimizem a transformação de dados.

Em resumo, um Mapping Task é uma tarefa que representa uma etapa de transformação de dados em um pipeline de processamento de dados, executada com base em regras definidas em um mapping.



### O que é um TaskFlow?

No Informatica Intelligent Cloud Services (IICS), um taskflow é uma sequência lógica de tarefas que são executadas em ordem para realizar uma integração de dados específica. Um taskflow pode incluir tarefas como extração de dados de fontes, transformação de dados, carregamento de dados em destinos, entre outras.

Os taskflows são criados usando a ferramenta de design do IICS, onde você pode arrastar e soltar tarefas em uma superfície de trabalho e definir as dependências entre elas. Você também pode adicionar controle de fluxo, como condições e loops, para controlar o fluxo de dados e a execução de tarefas.

Os taskflows são executados como trabalhos, que são instâncias de um taskflow que foram agendadas para execução. Você pode agendar trabalhos para serem executados uma vez, periodicamente ou a partir de eventos específicos.

Em resumo, um taskflow no IICS é uma sequência lógica de tarefas que são executadas em ordem para realizar uma integração de dados específica. Eles são criados usando a ferramenta de design do IICS e são executados como trabalhos.


### Qual a diferença entre Mapping e Taskflow?

Em Informatica Intelligent Cloud Services (IICS), um mapping e um taskflow são conceitos diferentes que servem para propósitos diferentes na integração de dados.

Um mapping é uma representação gráfica das regras de transformação que são aplicadas aos dados de entrada para produzir dados de saída. Ele define como os campos de entrada são convertidos em campos de saída, incluindo operações como agregação, filtragem, junção, entre outras. Um mapping é executado por uma tarefa de mapping, que é uma etapa do processo de integração de dados.

Já um taskflow é uma sequência lógica de tarefas que são executadas em ordem para realizar uma integração de dados específica. Ele pode incluir tarefas como extração de dados de fontes, transformação de dados, carregamento de dados em destinos, entre outras. Um taskflow pode incluir uma ou mais tarefas de mapping, mas também pode incluir outras tarefas, como tarefas de processamento de arquivos, tarefas de banco de dados, entre outras.

Em resumo, a diferença entre um mapping e um taskflow no IICS é que um mapping é uma representação gráfica das regras de transformação de dados, enquanto um taskflow é uma sequência lógica de tarefas que são executadas em ordem para realizar uma integração de dados específica.















