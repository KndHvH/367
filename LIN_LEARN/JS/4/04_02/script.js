

function detectBiggestNumber(x,y){
    if (x>y){
        return x
    } else if (y>x){
        return y
    }
    return 'equal'
}


detectBiggestNumber(1/2,1/4)