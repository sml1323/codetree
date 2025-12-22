board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.

drs = [1, 0, -1,1] # Right, down, leftDownDiagonal, rightDownDiagonal 
dcs = [0, 1, 1,1]

# move right or down or diagonal
def move(r,c, direction):
    r = r + drs[direction]
    c = c + dcs[direction]
    return r, c 

def check_condition(r,c):
    if 0 <= r < 19 and 0 <= c < 19:
        return True
    else:
        return False
            
# 오목 확인 
def check_OhMok(r, c, direction, current):
    five = 1
    for i in range(5):
        r, c = move(r, c, direction)
        if check_condition(r, c):
            if board[r][c] == current:
                five += 1
            else:
                break
    return five == 5

for r in range(19):
    for c in range(19):
        current = board[r][c]
        if current == 0:
            continue
        for d in range(4):
            if check_OhMok(r,c,d,current):
                print(current)
                print(r + drs[d] * 2 + 1,c + dcs[d] * 2 + 1)
                break
                

