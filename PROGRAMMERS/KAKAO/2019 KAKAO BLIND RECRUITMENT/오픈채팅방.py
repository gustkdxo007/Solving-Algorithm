def solution(record):
    status_dict = dict()
    answer = []
    for re in record:
        re = re.split()
        if re[0] == 'Enter':
            answer.append(([re[2], '님이 들어왔습니다.'], re[1]))
            status_dict[re[1]] = re[2]
        elif re[0] == 'Leave':
            answer.append(([status_dict[re[1]], '님이 나갔습니다.'], re[1]))
        elif re[0] == 'Change':
            status_dict[re[1]] = re[2]
    def change(rec):
        status, id = rec[0], rec[1]
        status[0] = status_dict[id]
        return ''.join(status)
    return list(map(change, answer))


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))