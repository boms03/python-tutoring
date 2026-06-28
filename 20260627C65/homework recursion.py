function checkVal(value){
    if (value == 0) {
        return 1
    }
        else {
        return value * checkVal(value -1)
    }
console.log(value)
checkVal(7);
}
