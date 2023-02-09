# IICS Component Architecture

## Informatica Cloud Service

- Metadata Repository
- Hosted, Multi-Tenant
- Managed by informatica
- Browser User Interface

## Informatica Secure Agent

- Execution Control
- Self-Updating
- Cloud, On-premise, or hosted
- No Data Storage



## Example:

![](pics/pic.png)






























# Glossario




### O que é PowerCenter Component Architecture Review ?

A revisão da arquitetura dos componentes do PowerCenter é o processo de avaliar e atualizar a estrutura atual dos componentes do PowerCenter para atender às necessidades atuais e futuras de integração de dados. Isso envolve avaliar as configurações atuais, processos e ferramentas, bem como identificar oportunidades de otimização, atualização ou substituição de componentes.

A revisão da arquitetura dos componentes do PowerCenter pode incluir a avaliação de componentes como:

-  Servidor de Repositório: para garantir que está funcionando corretamente e oferecendo as funcionalidades necessárias
-  Servidor de Integração: para verificar a eficiência de processamento de dados
-  Ferramentas de Mapeamento: para avaliar a eficiência e funcionalidade das regras de transformação de dados
-  Ferramentas de Workflow: para avaliar a eficiência e funcionalidade dos processos de ETL
-  Ferramentas de Monitoramento: para verificar a capacidade de monitorar e gerenciar o processo de integração de dados

A revisão da arquitetura dos componentes do PowerCenter é realizada por especialistas em integração de dados que trabalham com a organização para entender suas necessidades atuais e futuras e desenhar uma solução que atenda a essas necessidades. O objetivo é criar uma arquitetura escalável, confiável e eficiente que ajudará a organização a realizar integrações de dados de forma mais rápida e eficiente.



### O que é IICS Component Architecture

A arquitetura de componentes do Informatica Intelligent Cloud Services (IICS) é uma estrutura de componentes interconectados que trabalham juntos para fornecer as funcionalidades de integração de dados, governança de dados, análise de dados e gerenciamento de dados da plataforma. Cada componente tem uma função específica e trabalha em conjunto com outros componentes para fornecer uma solução completa e integrada.

Os componentes da arquitetura de componentes do IICS incluem, mas não se limitam a:

- Informatica Data Integration: permite a integração de dados de vários sistemas e fontes, incluindo sistemas de nuvem, sistemas on-premises e aplicativos de software como service (SaaS).

- Informatica Data Governance: oferece recursos de governança de dados, como definição de políticas, gerenciamento de metadados e conformidade regulatória.

- Informatica Data Quality: ajuda a garantir que os dados sejam precisos, completos e consistentes, oferecendo recursos de validação, correção e melhoria de dados.

- Informatica Big Data Management: permite a integração de dados em grande escala e a análise de dados não estruturados, como dados de log e dados de mídia social.

A arquitetura de componentes do IICS é projetada para oferecer uma solução completa e integrada para as necessidades de integração de dados, governança de dados, análise de dados e gerenciamento de dados das empresas. Isso permite que as empresas implementem soluções de maneira rápida e eficiente, com uma estrutura de componentes confiável e testada.

### O que é Informatica Secure Agent

Informatica Secure Agent é uma ferramenta da Informatica que permite a integração de dados em sistemas on-premises e cloud. É usado para estabelecer conexões seguras e confiáveis com fontes de dados em diferentes sistemas e locais, permitindo a transferência de dados de forma segura e eficiente.

O Informatica Secure Agent é projetado para garantir a segurança dos dados durante a transferência, usando criptografia e autenticação forte. Além disso, o Informatica Secure Agent é fácil de gerenciar e pode ser configurado para trabalhar de forma autônoma, sem intervenção manual. Isso ajuda a garantir que a integração de dados seja rápida, eficiente e confiável, sem prejudicar a segurança dos dados.

O Informatica Secure Agent é uma parte importante da plataforma de integração de dados da Informatica, ajudando as empresas a integrar dados de diferentes sistemas e fontes de maneira segura e confiável. Isso permite que as empresas obtenham insights valiosos a partir de seus dados e melhorem a eficiência dos processos de negócios.

### O que é Metadata Repository
Um repositório de metadados é um sistema de gerenciamento de dados que armazena informações sobre outros sistemas de dados e suas estruturas. O repositório de metadados é usado para documentar e gerenciar informações sobre os dados em um sistema, incluindo sua estrutura, relações, definições de campo e regras de negócios.

Os repositórios de metadados são importantes porque ajudam a garantir a qualidade dos dados e a consistência de sua estrutura, bem como a integridade dos processos de negócios que dependem desses dados. Eles também ajudam a facilitar a governança de dados, tornando mais fácil identificar e resolver problemas relacionados aos dados.

Além disso, os repositórios de metadados são úteis para a integração de dados, pois fornecem informações sobre as fontes de dados e suas estruturas, facilitando a integração de dados de diferentes sistemas. Eles também ajudam a garantir a consistência dos dados durante a integração, pois ajudam a identificar e corrigir quaisquer discrepâncias entre as fontes de dados.

Em resumo, um repositório de metadados é uma ferramenta importante para garantir a qualidade e a integridade dos dados em um sistema, bem como para facilitar a integração de dados e a governança de dados.

### O que é Multi-Tenant

Multi-Tenant é um modelo de arquitetura de software que permite que vários clientes compartilhem uma única instância de aplicativo ou infraestrutura. Em vez de cada cliente ter uma instância separada do software, todos os clientes compartilham a mesma instância, com recursos isolados para garantir que as informações de um cliente não sejam acessadas por outro cliente.

O modelo Multi-Tenant é muito comum em software como serviço (SaaS) e plataformas em nuvem, onde é possível fornecer serviços a vários clientes a partir de uma única instância do software. Isso permite aos provedores de serviços fornecer soluções escaláveis, eficientes e acessíveis a vários clientes, sem precisar fornecer uma instância separada do software para cada cliente.

Vantagens do modelo Multi-Tenant incluem redução de custos, pois é possível compartilhar recursos e infraestrutura, e facilidade de gerenciamento, pois é possível gerenciar vários clientes a partir de uma única instância do software. Além disso, o modelo Multi-Tenant é muito eficiente em termos de recursos, pois permite compartilhar recursos e otimizar o uso de hardware e infraestrutura.

Em resumo, o modelo Multi-Tenant é uma arquitetura de software que permite que vários clientes compartilhem uma única instância de aplicativo ou infraestrutura, oferecendo vantagens em termos de eficiência, escalabilidade, acessibilidade e gerenciamento de custos.



### O que é On-premise?

On-premise é uma arquitetura de software que significa que o software é instalado e executado localmente, em equipamentos próprios da organização. Em outras palavras, a organização compra o software e o instala em seus próprios servidores, em vez de acessá-lo através da nuvem ou de um provedor externo.

O modelo On-premise é contrastado com o modelo de software como serviço (SaaS), em que o software é acessado através da nuvem e é gerenciado pelo provedor.

O modelo On-premise oferece mais controle sobre o software e a infraestrutura, bem como mais privacidade e segurança dos dados, pois a organização mantém os dados e os recursos internamente. Além disso, o modelo On-premise é ideal para organizações que precisam de personalização e integração avançadas, que não são possíveis com soluções baseadas na nuvem.

No entanto, o modelo On-premise também pode ser mais caro e requerer mais esforço para gerenciar, pois a organização precisa manter a infraestrutura e garantir a disponibilidade do software. Além disso, o modelo On-premise pode ser menos escalável do que soluções baseadas na nuvem, pois a organização precisa adquirir mais recursos internamente.

Em resumo, o modelo On-premise é uma arquitetura de software que significa que o software é instalado e executado localmente, em equipamentos próprios da organização, oferecendo mais controle, privacidade e segurança, mas também maiores custos e esforços de gerenciamento.



















