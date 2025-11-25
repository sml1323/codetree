n, m = map(int, input().split())

# Please write your code here.

drs = [0, 1, 0, -1] # right down left up
dcs = [1, 0, -1, 0] 

# 알파벳
alphabet_idx = 0

# 0~25 : A-Z, 26~ : A~
def change_alphabet(alphabet_idx):
    return alphabet_idx % 26

# change direction
direction = 0
def change_direction(direction):
    return (direction + 1) % 4    



# condition
def is_in_range(r, c):
    return 0<=r<n and 0<=c<m

# move
def move(r, c, direction):
    r = r + drs[direction]
    c = c + dcs[direction]
    return r, c

# transform idx to alphabet
def make_alphabet(alphabet_idx):
    return chr(65 + alphabet_idx)



# init grid
grid = [[0] * m for _ in range(n) ]
r, c = 0, 0
alphabet_idx = 0
grid[r][c] = make_alphabet(alphabet_idx)
repeat_count = 1

while repeat_count < n * m:
    nr, nc = r + drs[direction], c + dcs[direction]
    if is_in_range(nr,nc) and grid[nr][nc] == 0:
        r, c = move(r, c, direction)
        alphabet_idx += 1
        repeat_count += 1
        alphabet_idx = change_alphabet(alphabet_idx)
        value = make_alphabet(alphabet_idx)
        grid[r][c] = value
    else:
        direction = change_direction(direction)
    

for row in grid:
    print(*row)
