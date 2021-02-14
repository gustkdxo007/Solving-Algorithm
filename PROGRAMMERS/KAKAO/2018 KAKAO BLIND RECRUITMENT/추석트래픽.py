from dateutil.parser import parse
from datetime import timedelta

def get_request(time, info):
    start = time
    end = start + timedelta(milliseconds=999)

    if info[0] <= start <= info[1] or (start <= info[0] and info[1] <= end) or info[0] <= end <= info[1]:
        return True
    return False

def solution(lines):
    answer = 0
    time_info = []
    for date in lines:
        tmp_date = date.split()
        end = parse(date[:23])
        start = end - timedelta(seconds=float(tmp_date[2][:-1]), milliseconds=-1)
        time_info.append([start, end])
    for log in time_info:
        for time in log:
            cnt = 0
            for info in time_info:
                if get_request(time, info):
                    cnt += 1
            answer = max(answer, cnt)
    return answer

print(solution([
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]))
print(solution([
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]))
print(solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))
