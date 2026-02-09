n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
# [1,2,3], [6,5,1]  -> 2XN개
# T : 반복 횟수
# 1. u, d 의 마지막 값 temp_u, temp_d 로 저장 후 하나씩 밀기, 이후 temp_d -> u, temp_u -> d

## 1. temp
for _ in range(t):
    temp_u, temp_d = u[-1], d[-1]
    ## 2. 하나씩 밀기
    for i in range(n-1, 0, -1):
        u[i] = u[i-1]
        d[i] = d[i-1]
    u[0] = temp_d
    d[0] = temp_u


print(*u)
print(*d)


        
    


