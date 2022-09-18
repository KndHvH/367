function display(){
    console.log('function test');
}

display();

function detectBiggestNumber(x,y){
    let biggest;

    x>y ? biggest = ['primeiro',x] : x<y ? biggest = ['segundo',y] : biggest = null;

    return biggest;
}

a = 3/6;
b = 6/13;

x = detectBiggestNumber(a,b);

x == null ? console.log('Numeros Iguais!') : console.log('O maior numero e o ' + x[0] + ' com o valor de ' + x[1])