# Cluster
- Conjunto de Computadores conectados e escalados de forma horizontal para resolver problemas de processamento em aplicacoes

## Master
- Compuatdor Principal, responsavel por gerenciar o cluster, manter e atualizar o estado desejado e receber e executar novos comandos

### Control Pane

- API - Receber e executar comandos, alem de manter uma comunicacao entre todos os componentes. E uma API Rest
- Control Manager - Manter e Atualizar o Estado desejado
- Scheduler - Onde cada POD vai ser executado dentro do Cluster
- ETCD - Banco de dados Chave Valor, para armazenar informacoes



## Node
- Em maior quantidade, responsavel por rodar os PODs

### Nodes
- Kubelet - Responsavel pela Execucao dos PODs
- K-proxy - Responsavel pela Comunicacao dos PODs



