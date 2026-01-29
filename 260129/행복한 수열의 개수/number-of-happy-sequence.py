n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

sol = 0
col = []
if m == 1:
    sol = 2 * n
    print(sol)

else:
    # 수열탐색... 행 탐색 후 열 탐색

    # 1. 행 탐색
    for row in grid:
        current = row[0]
        for i in range(1, n):
            if row[i] == current:
                sol += 1
                break
            else:
                current = row[i]
    # 2. 열 탐색
    for i in range(n):
        col.append([row[i] for row in grid])
        current = col[i][0]
        for c in range(1, n):
            if col[0][c] == current:
                sol += 1
                break
            else:
                current = col[i][c]
            
    print(sol)
                
            

