# def solution(s):
#     try:
#         if len(s) == 4 or len(s) == 6:
#             int(s)
#             return True
#         else:
#             return False
#     except:
#         return False

def solution(s):
    return s.isdecimal() and len(s) in [4, 6]


print(solution("a234"))
print(solution("1234"))