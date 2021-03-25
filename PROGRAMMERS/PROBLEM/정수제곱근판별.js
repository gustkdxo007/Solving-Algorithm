function solution(n) {
    const sqrt = Math.sqrt(n);
    return Number.isInteger(sqrt) ? (sqrt+1) ** 2 : -1;
}


console.log(solution(121));
console.log(solution(3));