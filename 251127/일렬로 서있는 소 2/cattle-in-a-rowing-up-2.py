N = int(input())
A = list(map(int, input().split()))

# Please write your code here.
sol = 0
A_length = len(A)

for i in range(A_length):
    for j in range(i + 1, A_length):
        for k in range(j + 1, A_length):
            if A[i] < A[j] < A[k]:
                sol += 1

print(sol)