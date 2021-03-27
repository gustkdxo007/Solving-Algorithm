function solution(n, m) {
    let GCM = 0;
    let LCM = [0, 0];
    for (let i=0; i<=m; i++) {
        if (!(n%i) && !(m%i)) {
            GCM = i;
            LCM = [parseInt(n/i), parseInt(m/i)];
        }
    }
    return [GCM, GCM*LCM[0]*LCM[1]]
}


console.log(solution(3, 12));
console.log(solution(2, 5));