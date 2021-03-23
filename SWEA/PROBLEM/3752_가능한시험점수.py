import sys
sys.stdin = open("../INPUT/3752.txt", "r")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    scores = [*map(int, input().split())]
    # 나올 수 있는 모든 조합의 점수를 배열에 표시
    sn = sum(scores)
    possible_scores = [0] * (sn + 1)
    possible_scores[0] = 1
    cnt = 1
    for score in scores:
        for i in range(sn, -1, -1):
            if possible_scores[i] and not possible_scores[i + score]:
                cnt += 1
                possible_scores[i+score] = 1
    print("#{} {}".format(t, cnt))
