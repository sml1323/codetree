n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
import sys


sol = sys.maxsize
for i in range(n):
    diff_sum = 0
    for j in range(n):
        if i != j:
            diff_sum += abs(i - j) * A[j] 
    sol = min(sol, diff_sum)
print(sol)


