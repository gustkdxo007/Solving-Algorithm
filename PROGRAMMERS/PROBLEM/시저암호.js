function solution(s, n) {
    return s.split('').map(val => {
        charCode = val.charCodeAt()
        if (97 <= charCode && charCode <= 122) {
            return String.fromCharCode(97 * parseInt((charCode + n) / 123) + ((charCode + n) % 123) );
        } else if (65 <= charCode && charCode <= 90) {
            return String.fromCharCode(65 * parseInt((charCode + n) / 91) + ((charCode + n) % 91))
        } else {
            return ' '
        }
    }).join('')
}


console.log(solution("AB", 1))
console.log(solution("z", 1))
console.log(solution("a B z", 4))