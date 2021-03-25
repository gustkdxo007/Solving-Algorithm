function solution(s) {
    s = s.split(' ');
    s = s.map(str => {
        new_str = '';
        for(let i = 0; i < str.length; i++) {
            if (i % 2) {
                new_str += str[i].toLowerCase();
            } else {
                new_str += str[i].toUpperCase();
            }
        }
        return new_str;
    })
    return s.join(' ');
}


console.log(solution("try hello world"));