def change_time_to_int(input_time):
    hour, minute, second = input_time[:2], input_time[3:5], input_time[6:]
    time = int(hour) * 3600 + int(minute) * 60 + int(second)
    return time

def change_time_to_str(time):
    hour = time // 3600
    time = time % 3600
    minute = time // 60
    time = time % 60
    hour = str(hour).zfill(2)
    minute = str(minute).zfill(2)
    second = str(time).zfill(2)
    return hour + ":" + minute + ":" + second

def solution(play_time, adv_time, logs):
    answer = 0
    play_time = change_time_to_int(play_time)
    adv_time = change_time_to_int(adv_time)
    logs = [*map(lambda log: (change_time_to_int(log[:8]), change_time_to_int(log[9:])), logs)]
    runtime = [0] * (play_time + 1)

    # 시간 초과 발생
    # for s, e in logs:
    #     for i in range(s, e):
    #         runtime[i] = runtime[i] + 1

    for s, e in logs:
        runtime[s] += 1
        runtime[e] -= 1

    for i in range(1, play_time+1):
        runtime[i] += runtime[i-1]
    for i in range(1, play_time+1):
        runtime[i] += runtime[i-1]

    max_view = 0
    for i in range(adv_time-1, play_time):
        if i - adv_time < 0:
            max_view = runtime[i]
            answer = i - adv_time + 1
        else:
            if max_view < runtime[i] - runtime[i-adv_time]:
                max_view = runtime[i] - runtime[i-adv_time]
                answer = i - adv_time + 1
    return change_time_to_str(answer)


print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))