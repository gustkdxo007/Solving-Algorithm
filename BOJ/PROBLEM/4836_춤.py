import sys
sys.stdin = open("../INPUT/4836.txt", "r")

def step_1(arr):
    check = True
    for i in range(len(arr)):
        if arr[i] == 'dip':
            if i - 1 >= 0 and arr[i-1] == 'jiggle': pass
            elif i - 2 >= 0 and arr[i-2] == 'jiggle': pass
            elif i + 1 < len(arr) and arr[i+1] == 'twirl': pass
            else:
                arr[i] = 'DIP'
                check = False
    return check

def step_2(arr):
    if len(arr) < 3: return False
    if arr[-3] != 'clap' or arr[-2] != 'stomp' or arr[-1] != 'clap': return False
    return True

def step_3(arr):
    if 'twirl' in arr:
        if 'hop' in arr:
            return True
        return False
    return True

def step_4(arr):
    if arr[0] == 'jiggle': return False
    return True

def step_5(arr):
    return 'dip' in arr or 'DIP' in arr


while True:
    check = set()
    try:
        input_list = input().split()
        if not step_1(input_list):
            check.add('1')
        if not step_2(input_list):
            check.add('2')
        if not step_3(input_list):
            check.add('3')
        if not step_4(input_list):
            check.add('4')
        if not step_5(input_list):
            check.add('5')
        check = list(check)
        str = ' '.join(input_list)
        if len(check) == 0:
            print('form ok: ' + str)
        else:
            if len(check) == 1:
                print(f'form error {check[0]}: {str}')
            else:
                e = ''
                check.sort()
                for i in range(len(check)):
                    e += check[i]
                    if i == len(check) - 2:
                        e += ' and '
                    elif i != len(check) - 1:
                        e += ', '
                print(f'form errors {e}: {str}')
    except:
        break



