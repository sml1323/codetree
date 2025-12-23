N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# Please write your code here.

# 방향
drs = [0, 1, 0, -1, 1, 1, -1, -1] # right, down, left, up, right up diagonal, right down diagonal,
dcs = [1, 0, -1, 0, -1, 1, -1, 1] # left up diagonal, left down diagonal

# inrange
def in_range(r,c):
    if 0 <= r < N and 0 <= c < M:
        return True

# LEE 검증 함수 
def is_LEE(r, c, direction):
    """value 가 L일때, 그 뒤 값이 연속으로 EE 인지 8방향 2번 검사"""
    count = 0
    for i in range(2):
        r = r + drs[direction]
        c = c + dcs[direction]
        if in_range(r,c) and arr[r][c] == "E":
            count += 1
    
    if count == 2:
        return True 
    else:
        return False
sol = 0
for r in range(N):
    for c in range(M):
        if arr[r][c] == "L":
            for direction in range(8):
                if is_LEE(r,c,direction):
                    sol += 1
print(sol)
            
        




