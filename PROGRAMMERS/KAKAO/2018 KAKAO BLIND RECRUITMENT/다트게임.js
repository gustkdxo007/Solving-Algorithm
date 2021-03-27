function solution(dartResult) {
    const result = [];
    [...dartResult].forEach((val, i) => {
        const idx = ['', 'S', 'D', 'T'].indexOf(val);
        if (parseInt(val) >= 0) {
            if (!parseInt(val) && i && parseInt(dartResult[i-1])) return;
            if (parseInt(dartResult[i+1]) >= 0) {
                result.push(parseInt(val+dartResult[i+1]));
            } else {
                result.push(parseInt(val));
            }
        } else if (idx > 0) {
            result[result.length-1] **= idx;
        } else if (val === '*') {
            if (result.length > 1) {
                result[result.length-2] *= 2;
            }
            result[result.length-1] *= 2;
        } else if (val === '#') {
            result[result.length-1] *= (-1);
        }
    })
    return result.reduce((acc, cur) => acc + cur);
}


console.log(solution("1S2D*3T"));
console.log(solution("1D2S#10S"));
console.log(solution("1D2S0T"));
console.log(solution("1S*2T*3S"));
console.log(solution("1D#2S*3S"));
console.log(solution("1T2D3D#"));
console.log(solution("1D2S3T*"));