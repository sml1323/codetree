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
        current_happy = 1
        current = row[0]
        for i in range(1, n):
            if row[i] == current:
                current_happy += 1
                if current_happy == m:
                    sol += 1
                    break
            else:
                current = row[i]
                current_happy = 1
    # 2. 열 탐색
    for i in range(n):
        col.append([row[i] for row in grid])
        current = col[i][0]
        current_happy = 1
        for c in range(1, n):
            if col[i][c] == current:
                current_happy += 1
                if current_happy == m:
                    sol += 1
                    break
            else:
                current = col[i][c]
                current_happy = 1
            
    print(sol)

  
            

