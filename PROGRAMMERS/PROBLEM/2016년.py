# import datetime
#
# def solution(a, b):
#     week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
#     return week[datetime.date(2016, a, b).weekday()]


def solution(a, b):
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ans = 0
    for m in range(a):
        ans += day[m]
    ans += (b-1)
    answer = week[ans%7]
    return answer


print(solution(5, 24))