function solution(n, arr1, arr2) {
    return arr1.map((val, idx) => {
        // console.log((val | arr2[idx]).toString(2))
        const val1 = val.toString(2).padStart(n, '0');
        const val2 = arr2[idx].toString(2).padStart(n, '0');
        return [...val1].reduce((acc, cur, idx) => cur === '0' && val2[idx] === '0' ? acc + ' ' : acc + '#', '');
    })
}


console.log(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]));
console.log(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]));