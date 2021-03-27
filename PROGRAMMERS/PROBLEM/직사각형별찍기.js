function solution(a, b) {
    Array.from(Array(b), () => console.log(Array(a).fill('*').join('')));
}


console.log(solution(5, 3));