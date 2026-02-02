n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


# 격자 최대 크기 = 20 X 20 = 400
## 최대 점수: 400 X 10 = 4000
### 최대 cost: K^2 + (K+1)^2 = 2K^2
### 2K^2 = 4000, K^2 = 2000, K < 2000^(1/2) == 45정도 보다 작아야 의미있음(넘으면 cost가 점수보다 커 무의미함)



sol = 0
for r in range(n):
    for c in range(n):
        for K in range(45):
            cnt = 0
            for dr in range(-K, K + 1):
                nr = r + dr
                if nr < 0 or nr >= n:
                    continue
                remain = K - abs(dr)
                left = c - remain
                right = c + remain

                for nc in range(left, right + 1):
                    if 0 <= nc < n and grid[nr][nc] == 1:
                        cnt += 1
            cost = K * K + (K + 1) * (K + 1)
            if cnt * m >= cost:
                sol = max(cnt, sol)

print(sol)
