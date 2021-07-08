import sys
sys.stdin = open('../INPUT/1259.txt', 'r')

while True:
    tc = input()
    if not int(tc):
        break
    check = True
    for i in range(len(tc)//2 + 1):
        if tc[i] != tc[-i-1]:
            check = False
            print('no')
            break
    if check:
       print('yes')