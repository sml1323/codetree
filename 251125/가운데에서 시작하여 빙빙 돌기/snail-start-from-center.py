n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.




# dr,dc
dr = [0, -1, 0, 1] # right, up, left, down
dc = [1, 0, -1, 0]


def change_direction(direction):
    return (direction + 1) % 4

def move(r,c, direction):
    return r + dr[direction], c + dc[direction]

# create grid
grid = [[0] * n for _ in range(n)]

# init value
# 가운데 시작: N // 2
start = n // 2
r, c = start, start
direction = 0
num = 1
grid[r][c] = num
limit = 2
moving_number = 1
moving_count = {moving_number:2}

# 1칸 두번, 2칸 두번, 3칸 두번, 4칸 두번 
# moving_number 만큼 이동 시 count[number] 빼줌 
# 0이되면 moving_number += 1


while num < n*n:
    if moving_count[moving_number] > 0: # 횟수 증가할지  
        for _ in range(moving_number): 
            if num >= n*n:
                break
            r, c = move(r, c, direction)
            num += 1
            grid[r][c] = num
        moving_count[moving_number] -= 1
        direction = change_direction(direction)
    else:
        moving_number += 1
        moving_count[moving_number] = limit

for row in grid:
    print(*row)




