function solution(x) {
    return !(x % (x+'').split('').reduce((acc, cur) => parseInt(acc) + parseInt(cur)));
}


console.log(solution(10));
console.log(solution(12));
console.log(solution(11));
console.log(solution(13));