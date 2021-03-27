function solution(numbers, hand) {
    let answer = "";
    const left = [1, 4, 7];
    const right = [3, 6, 9];
    const middle = [2, 5, 8, 0];
    let leftIdx = [0, 3];
    let rightIdx = [2, 3];
    numbers.forEach(val => {
        if (left.indexOf(val) > -1) {
            leftIdx = [0, left.indexOf(val)];
            answer += "L";
        } else if (right.indexOf(val) > -1) {
            rightIdx = [2, right.indexOf(val)];
            answer += "R";
        } else {
            let middleIdx = [1, middle.indexOf(val)];
            let leftGap = Math.abs(leftIdx[0]-middleIdx[0]) + Math.abs(leftIdx[1]-middleIdx[1]);
            let rightGap = Math.abs(rightIdx[0]-middleIdx[0]) + Math.abs(rightIdx[1]-middleIdx[1]);
            if (leftGap > rightGap) {
                answer += "R";
                rightIdx = middleIdx;
            } else if (rightGap > leftGap) {
                answer += "L";
                leftIdx = middleIdx;
            } else {
                if (hand === "right") {
                    answer += "R";
                    rightIdx = middleIdx;
                } else if (hand == "left") {
                    answer += "L";
                    leftIdx = middleIdx;
                }
            }
        }
    })
    return answer;
}


console.log(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"));
console.log(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"));
console.log(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"));