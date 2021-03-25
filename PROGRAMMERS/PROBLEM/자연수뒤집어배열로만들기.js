function solution(n) {
    return (n+"").split('').reverse().map(val => parseInt(val));
}



console.log(solution(12345))