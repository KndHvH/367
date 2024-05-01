# Http

## Http (request - response)
- Uma requisicao precisa ter todas as informacoes para ter as resposta
- Http e *Stateless* (nao guarda informacoes entre requisicoes)
- para guardar informacoes precisamos de Sessoes, Cokkies

### Error codes
- 2XX - Sucess
- 3XX - Redirect
- 4XX - Client Error
- 5XX - server Error

### Methods
- GET - Cliente usca dados do server, por meio de parametros na url
- POST - Cliente Submete dados ao server, por meio de parametros no corpo do request
- DELETE - Remove recurso
- PUT - Atualiza recurso 

### Accept
- Accept: text/html, Accept: text/css, Accept: application/xml, Accept: application/json, Accept:image/jpeg e Accept: image/-asterisco

- Accept: */*

### Keep Alive
- Determina quanto tempo a conexao tcp fica ativa, permitindo multiplas requisicoes pela mesma conexao


## Http2

### Headers
- binarios
- comprimidos com HPACK
- Header Stateful - mandamos apenas os cabecalhos que mudam

### Body - resposta
- comprimidos com gzip

### Multiplexing
- Multiplos requests sendo realizados em paralelo, de forma independente com uma conexao tcp

### Server Push
- Retorna dados antes que o cliente precise pedir, por meio na analise do html
