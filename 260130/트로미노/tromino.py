n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# 기본 프로세스: 탐색 함수 + in_range 함수 , 범위 안이라면 탐색하고 기록
def in_range(r,c):  # max_r, max_c 로 확인해야함
    return 0 <= r < n and 0 <= c < m


# 블록 1번: 가로 또는 세로 3개
## 모양대로 탐색하기
### 1. 가로 
def check_horizen(r,c):
    return grid[r][c] + grid[r][c+1] + grid[r][c+2]
    
### 2. 세로
def check_verticle(r,c):
    return grid[r][c] + grid[r+1][c] + grid[r+2][c]

# 블록 2번: ㄴ 모양, ㄴ 반대 모양, ㄱ 반대 모양, ㄱ 모양
## 1. ㄴ 
def check_s(r,c):
    return grid[r][c] + grid[r+1][c] + grid[r+1][c+1]

## 2. reverse ㄴ
def check_reverse_s(r,c):
    return grid[r][c] + grid[r+1][c] + grid[r+1][c-1]

## 3. ㄱ
def check_r(r,c):
    return grid[r][c] + grid[r][c+1] + grid[r+1][c+1]

## 4. reverse ㄱ
def check_reverse_r(r,c):
    return grid[r][c] + grid[r][c-1] + grid[r+1][c-1]
    




def check_linear(r,c):
    max_value = 0
    if in_range(r,c + 2):
        max_value = max(max_value, check_horizen(r,c))
    if in_range(r+2,c):
        max_value = max(max_value, check_verticle(r,c))
    return max_value

def check_triblock(r,c):
    max_value = 0
    if in_range(r+1,c+1):
        max_value = max(max_value, check_s(r,c))
    if in_range(r+1, c-1):
        max_value = max(max_value, check_reverse_s(r,c))
    if in_range(r+1,c+1):
        max_value = max(max_value, check_r(r,c))
    if in_range(r+1,c-1):
        max_value = max(max_value, check_reverse_r(r,c))
    return max_value

sol = 0
for r in range(n):
    for c in range(m):
        current_max = max(check_linear(r,c), check_triblock(r,c), 0)
        sol = max(current_max, sol)

print(sol)
        



