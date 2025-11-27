A = input()

# Please write your code here.

sol = 0
for i in range(len(A)):
    if A[i] == "(":
        for j in range(i + 1, len(A)):
            if A[j] == ")":
                sol += 1

print(sol)
