import sys
sys.setrecursionlimit(100000000)

def find_room(room_n, rooms):
    if room_n not in rooms:
        rooms[room_n] = room_n + 1
        return room_n
    empty_room = find_room(rooms[room_n], rooms)
    rooms[room_n] = empty_room + 1
    return empty_room

def solution(k, room_number):
    answer = []
    rooms = dict()
    for r in room_number:
        answer.append(find_room(r, rooms))
    return answer


print(solution(10, [1,3,4,1,3,1]))