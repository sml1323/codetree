A = input()

# Please write your code here.

length = len(A)

count = 0

for i in range(length - 1):
    if A[i] == '(' and A[i + 1] == '(':
        for j in range(i + 2, length - 1):
            if A[j] == ')' and A[j + 1] == ')':
                count += 1

print(count)





