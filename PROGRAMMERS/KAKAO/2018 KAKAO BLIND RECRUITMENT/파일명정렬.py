def solution(files):
    new_arr = []
    for file in files:
        head = ''
        num = ''
        tail = ''
        check = True
        for i in range(len(file)):
            if 48 <= ord(file[i]) <= 57:
                num += file[i]
                check = False
                continue
            if not check:
                tail = file[i:]
                break
            head += file[i]
        new_arr.append((head, num, tail))
    new_arr.sort(key=lambda x: (x[0].lower(), int(x[1])))
    new_arr = [*map(''.join, new_arr)]
    return new_arr


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
print(ord('0'), ord('9'))