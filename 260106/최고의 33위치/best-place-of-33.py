n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def in_grid(r,c):
    return 0 <= r + 2 <= n - 1 and 0 <= c + 2 <= n - 1


def count_of_coin(r,c):
    count = 0
    for i in range(3):
        for j in range(3):
            count += grid[r + i][c + j]
    return count

sol = 0
for r in range(n):
    for c in range(n):
        if in_grid(r,c):
            sol = max(count_of_coin(r,c), sol)
        else:
            break
print(sol)    
