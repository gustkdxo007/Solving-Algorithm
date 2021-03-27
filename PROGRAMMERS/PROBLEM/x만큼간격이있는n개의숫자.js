function solution(x, n) {
    const answer = new Array(n).fill(0);
    answer[0] = x;
    for (let i=1; i<n; i++) {
        answer[i] = answer[i-1] + x;
    }
    return answer;
}


console.log(solution(2, 5));
console.log(solution(4, 3));
console.log(solution(-4, 2));