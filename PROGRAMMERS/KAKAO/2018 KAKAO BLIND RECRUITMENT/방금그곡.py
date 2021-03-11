def change_code(code):
    code = code.replace('C#', 'c')
    code = code.replace('D#', 'd')
    code = code.replace('F#', 'f')
    code = code.replace('G#', 'g')
    code = code.replace('A#', 'a')
    return code

def solution(m, musicinfos):
    answer = []
    m = change_code(m)

    for music in musicinfos:
        start, end, title, info = music.split(',')
        # 시간을 분으로 변경
        start = int(start[:2]) * 60 + int(start[3:])
        end = int(end[:2]) * 60 + int(end[3:])
        # 플레이 시간
        runtime = end - start
        # 재생 곡 정보
        info = change_code(info)
        if runtime <= len(info):
            info = info[:runtime]
        else:
            info *= runtime // len(info)
            info += info[:runtime%len(info)]
        if m in info:
            if not answer:
                answer = [runtime, title]
            elif answer[0] < runtime:
                answer = [runtime, title]
    return answer[1] if answer else '(None)'


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("DEF", ["12:00,12:14,HELLO,C#DEF#GAB", "13:00,13:06,WORLD,ABCDEF"]))
