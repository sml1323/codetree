n = int(input())
S = input()

# Please write your code here.
length = len(S)

sol = 0
for i in range(length - 2):
    if S[i] != 'C':
        continue
    for j in range(i + 1, length - 1):
        if S[j] != 'O':
            continue
        for k in range(j + 1, length):
            if S[k] == 'W':
                sol += 1

print(sol)         





