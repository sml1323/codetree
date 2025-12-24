n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def in_range(r,c):
    return 0 <= r < n and 0 <= c < n

count_dict = {
    0: 0,
    1: 0,
    2: 0,
    3: 0
}

def count_one(r,c):
    count = 0
    for i in range(0, 3):
        count += arr[r][c + i]
    return count
        
        

for r in range(n):
    for c in range(n):
        if in_range(r, c+2):
            count_dict[count_one(r,c)] += 1
sol = 0
count = 0

if count_dict[3] >= 2:
    sol = 6
elif count_dict[3] == 1:
    if count_dict[2]:
        sol = 5
    elif count_dict[1]:
        sol = 4
    else:
        sol = 3
else:
    if count_dict[2] >= 2:
        sol = 4
    elif count_dict[2]:
        if count_dict[1]:
            sol = 3
        else:
            sol = 2
print(sol)

    


