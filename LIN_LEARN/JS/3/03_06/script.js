var a = 5;
var b = 4;
var c = 4;

//and
if (a===b && b===c){
    console.log('primeira cond')

    //or
}else if (a===b || b===c){
    console.log('segunda cond')
}



d = 4
e = 5
f = 6
g = 6

//XOR

if (!(d==e && f==g)){
    if (d==e || f==g){
        console.log('Xor success')
    }
}


//ternario

d != e ? console.log('ternario') : console.log('failure')