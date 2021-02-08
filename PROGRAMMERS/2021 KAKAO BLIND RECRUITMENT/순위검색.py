import bisect

def make_comb(data, s, result):
    global info_dict
    if len(result) == 4:
        comb = ''.join(result)
        if comb in info_dict:
            info_dict[comb].append(int(data[4]))
        else:
            info_dict[comb] = [int(data[4])]
        return
    # for i in range(2):
    #     if i == 0:
    result.append(data[s])
    make_comb(data, s+1, result)
    result.pop()
        # elif i == 1:
    result.append('-')
    make_comb(data, s+1, result)
    result.pop()

info_dict = dict()

def solution(info, query):
    global condition
    answer = []
    for data in info:
        make_comb(data.split(), 0, [])
    for ans in info_dict.keys():
        info_dict[ans].sort()
    for q in query:
        que = q.split()
        cond = ''
        score = int(que[-1])
        for q in que[:-1]:
            if q == 'and': continue
            cond += q
        if cond in info_dict:
            cnt = len(info_dict[cond]) - bisect.bisect_left(info_dict[cond], score)
            answer.append(cnt)
        else:
            answer.append(0)
    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))