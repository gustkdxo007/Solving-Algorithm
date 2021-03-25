function solution(n) {
    return parseInt((n+'').split('').sort().reverse().join(''));
}


console.log(solution(118372))