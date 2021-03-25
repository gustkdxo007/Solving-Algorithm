function solution(n) {
    return n.toString().split('').reduce((acc, val) => acc + parseInt(val), 0);
}

console.log(solution(123));
console.log(solution(987));