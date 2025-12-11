n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.

# 거리 계산 함수 
def cal_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

total_distance = 0
for i in range(n - 1):
    total_distance += cal_distance(points[i], points[i + 1])


min_distance = total_distance

for i in range(1, n - 1):
    # 1번 체크포인트를 건너 뛴다면 0-1, 1-2 를 제거하고, 0-2를 추가해야함 
    remove_distance = cal_distance(points[i - 1], points[i]) + cal_distance(points[i], points[i + 1])
    add_distance = cal_distance(points[i - 1], points[i + 1])
    
    temp_distance = total_distance - remove_distance + add_distance
    min_distance = min(temp_distance, min_distance)

print(min_distance)



