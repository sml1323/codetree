n, m = map(int, input().split())

# Please write your code here.


# down right up left
dxs = [1, 0, -1, 0] # 행
dys = [0, 1, 0, -1] # 열 

# init grid
grid = [[0] * m for _ in range(n)]
# init direction
direction = 0
x, y = 0, 0
grid[x][y] = 1
num = 1
def is_boundary(x,y):
    return 0 <= x < n and 0 <= y < m 

def is_visited(x,y):
    """visited: False"""
    return grid[x][y] == 0

def change_direction(direction):
    return (direction + 1) % 4

def move(x, y, direction):
    nx = x + dxs[direction]
    ny = y + dys[direction]
    return nx, ny 

while num < n * m:
    nx, ny = x + dxs[direction], y + dys[direction]
    if is_boundary(nx, ny) and is_visited(nx, ny):
        x, y = move(x, y, direction)
        num += 1
        grid[nx][ny] = num
    else:
        direction = change_direction(direction)

for row in grid:
    for col in row:
        print(col, end=" ")
    print()
        
        

