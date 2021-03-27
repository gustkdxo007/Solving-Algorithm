function solution(arr1, arr2) {
//     const N = arr1.length;
//     const M = arr1[0].length;
//     const answer = Array.from(Array(N), () => Array(M).fill(0));
//     for (let i=0; i < N; i++) {
//         for (let j=0; j < M; j++) {
//             answer[i][j] = arr1[i][j] + arr2[i][j];
//         }
//     }
//     return answer;
    return arr1.map((a, i) => a.map((b, j) => b + arr2[i][j]));
}



console.log(solution([[1,2],[2,3]], [[3,4],[5,6]]));
console.log(solution([[1],[2]],[[3],[4]]))