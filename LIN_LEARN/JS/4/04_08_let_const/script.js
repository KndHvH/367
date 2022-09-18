const banana = 7;

console.log(banana);


// banana = 8;  (error)


function logScope() {
    let localVar = 4;

    if (localVar) {
        let localVar = "Eu sou diferente"
        console.log("Var local aninnhada: ", localVar);
    }
    console.log("Var local: ", localVar);
}

logScope();


// var = global
// let = nao tao global
// const = constante