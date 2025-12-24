N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

# 두개를 제외한 모든 합 리스트 생성
sums = []
for i in range(N - 1):
    for j in range(i, N):
        sums.append(abs((sum(arr) - (arr[i] + arr[j])) - S))

sums = sorted(sums)
print(sums[0])
