function Pessoa(nome, sobrenome, idade, sexo) {
    this.nome = nome,
    this.sobrenome = sobrenome,
    this.idade = idade,
    this.sexo = sexo,
    this.aniversario = function () {
        return ++idade;
    }
}

pessoas = [
    new Pessoa('duda', 'maciel', 19, 'feminino'),
    new Pessoa('matias', 'herklotz', 20, 'masculino'),
    new Pessoa('octavio', 'almeida', 19, 'masculino'),
    new Pessoa('blair')
]