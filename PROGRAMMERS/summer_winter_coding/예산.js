function solution(d, budget) {
    d = d.sort((a, b) => a - b);
    let answer = 0;
    let sum = 0;
    d.forEach((val) => {
        sum += val;
        if (sum > budget) {
            return answer;
        }
        answer += 1
    })
    return answer;
}


console.log(solution([1,3,2,5,4], 9));
console.log(solution([2,2,3,3], 10));