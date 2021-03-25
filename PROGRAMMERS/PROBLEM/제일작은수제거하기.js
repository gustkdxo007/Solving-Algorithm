function solution(arr) {
    const min_idx = arr.indexOf(Math.min(...arr));
    // const min_idx = arr.indexOf(Math.min.apply(null, arr));
    arr.splice(min_idx, 1);
    return arr.length ? arr : [-1]
}


console.log(solution([4,3,2,1]));
console.log(solution([10]));