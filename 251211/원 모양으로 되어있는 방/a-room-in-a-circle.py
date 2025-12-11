n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.
import sys

human_dict = {}
for i in range(1, n + 1):
    human_dict[i] = a[i - 1]

# 1에서 시작: (1 - 2) x human_dict[2], (1 - 3) x human_dict[3]...
# 만약 이동 방이 번호가 작다면: 2 -> 1 : 3 4 5 1 거리 4. 

def calculate(start_room, moving_room):
    if start_room > moving_room:
        dist = n - (start_room - moving_room)       
    else:
        dist = moving_room - start_room
    return  dist * human_dict[moving_room]


distance = sys.maxsize

def moving_distance(start_room):
    move_distance = 0
    for i in range(1,n + 1):
        move_distance += calculate(start_room, i)
    return move_distance

for start_room in range(1, n + 1):
    distance = min(moving_distance(start_room), distance)

print(distance)
    
    
    



