N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.

dr = [-1, 0, 1, 0] # up(init), right, down, left
dc = [0, 1, 0, -1]




def change_direction(direction, string):
    return (direction + 1) % 4 if string == "R" else (direction -1) % 4

def in_range(nr, nc):
    return 0 <= nr < N and 0 <= nc < N

def move(r, c, direction):
    nr, nc = r + dr[direction], c + dc[direction]
    return nr, nc
# init variables
direction = 0
init_position = N // 2 # mid
r, c = init_position, init_position
sol = board[r][c]

for string in str:
    nr, nc = r + dr[direction], c + dc[direction]
    if string == "F":
        if in_range(nr, nc):
            r, c = nr, nc
            sol += board[r][c]
    else:
        direction = change_direction(direction, string)

print(sol)




 