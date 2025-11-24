n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.

# 위에서: \ : 오른쪽으로, x + 1, / : 왼쪽으로, x - 1,
# 오른쪽에서: \: 위로, y - 1, / : 아래로, y + 1
# 아래에서: \ : 왼쪽으로, x - 1, / : 오른쪽으로, x + 1
# 왼쪽에서: \ : 아래로, y + 1 , / : 위로, y - 1

# backslash, slash mapping direction
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]


backslash = {
    "down": (dxs[1], dys[1], "right"),
    "right": (dxs[0], dys[0], "down"),
    "left": (dxs[2], dys[2], "up"),
    "up": (dxs[3], dys[3], "left")
}

slash = {
    "down": (dxs[3], dys[3], "left"),
    "right": (dxs[2], dys[2], "up"),
    "left": (dxs[0], dys[0], "down"),
    "up": (dxs[1], dys[1], "right")
}



# 종료 조건은 index > n
# init direction
init_direction = (0, 0, "")
if k <= n:
    init_direction = (0, k - 1, "down")
    
elif n < k <= 2*n:
    init_direction = (n - 1, k - n - 1, "left")
elif 2*n < k <= 3*n:
    
    init_direction = (n - 1,3*n - k - 1, "up")
else:
    init_direction = (4*n - k - 1, 0, "right")

def check(x, y):
    return 0 <= x < n and 0 <= y < n

sol = 1
x, y = init_direction[0], init_direction[1]
direction = init_direction[2]
while True:
    
    if grid[x][y] == "\\":
        nx, ny, direction = backslash[direction]
        x , y = x + nx, y + ny
        if check(x, y):
            sol += 1
        else:
            break
    else:
        nx, ny, direction = slash[direction]
        x , y = x + nx, y + ny
        if check(x, y):
            sol += 1
        else:
            break
print(sol)
    

    


    

