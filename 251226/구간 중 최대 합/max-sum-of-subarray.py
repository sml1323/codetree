n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
max_value = 0
for i in range(n - k + 1):
    value = 0
    for j in range(i, i + k):
        value += arr[j]
    
    max_value = max(max_value, value)


print(max_value)