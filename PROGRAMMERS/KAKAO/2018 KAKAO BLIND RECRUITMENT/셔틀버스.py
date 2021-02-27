def solution(n, t, m, timetable):
    answer = 0
    bus_time = [540]
    for i in range(n-1):
        bus_time.append(bus_time[-1] + t)
    def timeToMinute(time):
        arr = time.split(':')
        return int(arr[0])*60 + int(arr[1])
    timetable = list(map(timeToMinute, timetable))
    timetable.sort()
    bus_arrived = 540 - t
    last = 0
    bus_cnt = 0
    for i in range(n):
        bus_arrived += t
        bus_cnt = 0
        while timetable and bus_cnt < m:
            if timetable[0] <= bus_arrived:
                bus_cnt += 1
                last = timetable.pop(0)
            else:
                break
    if bus_cnt < m:
        answer = bus_arrived
    else:
        answer = last - 1
    return str(answer//60).zfill(2) + ':' + str(answer%60).zfill(2)



print(solution(2, 1, 3, ["08:00","08:00","08:01","08:01", "08:07", "08:08"]))
print(solution(2, 9, 2, ["09:10","09:09","08:00"]))
print(solution(2, 1, 2, ["09:00","09:00","09:00","09:00"]))
print(solution(1, 1, 5, ["00:01","00:01","00:01","00:01","00:01"]))
print(solution(1, 1, 1, ["23:59"]))
print(solution(10, 60, 45, 	["23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59"]))
