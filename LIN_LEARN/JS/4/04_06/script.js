a = 1/2
b = 9/10

var theBiggest = function(x,y) {
    var result
    x > y ? result = [1,x] : result = [2,y]
    return result
}(a,b);

console.log(theBiggest)