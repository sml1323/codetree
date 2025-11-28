R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.


# 처음 발판이 무엇인지 확인 후 다음 발판까지 가능한 경우의 수 계산 
# 경우의 수: W B W B or B W B W
init_foothold = grid[0][0]
foothold_r, foothold_c = 0 , 0
jump = 0

middle_point = []
# if W B W B

sol = 0
if init_foothold == "W":
    for i in range(foothold_r + 1, R-1):
        for j in range(foothold_c + 1, C-1):
            if grid[i][j] == "B":
                # 리스트에 저장 후 이후 순회 
                middle_point.append((i,j))

    for point in middle_point:
        foothold_r, foothold_c = point[0], point[1]
        for i in range(foothold_r + 1, R - 1):
            for j in range(foothold_c + 1, C - 1):
                if grid[i][j] == "W":
                    sol += 1    
else:
    for i in range(foothold_r + 1, R-1):
        for j in range(foothold_c + 1, C-1):
            if grid[i][j] == "W":
                # 리스트에 저장 후 이후 순회 
                middle_point.append((i,j))
    for point in middle_point:
        foothold_r, foothold_c = point[0], point[1]
        for i in range(foothold_r + 1, R - 1):
            for j in range(foothold_c + 1, C - 1):
                if grid[i][j] == "B":
                    sol += 1


print(sol)





