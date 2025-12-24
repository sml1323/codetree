n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def in_range(r,c):
    return 0 <= r < n and 0 <= c < n

# 점수, 행, 열
grid_list = []



def count_one(r,c):
    count = 0
    for i in range(0, 3):
        count += arr[r][c + i]
    return count
        
        

for r in range(n):
    for c in range(n):
        if in_range(r, c+2):
            grid_list.append((count_one(r,c), r, c))

sol = 0
grid_list = sorted(grid_list, reverse=True)

for i in range(len(grid_list) - 1):
    for j in range(1, len(grid_list)):
        if grid_list[i][1] != grid_list[j][1] or abs(grid_list[i][2] - grid_list[j][2]) >= 3:
            sol = max(grid_list[i][0] + grid_list[j][0], sol)
            

print(sol)


