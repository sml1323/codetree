n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.

length = len(arr)

# validate no carry
def is_carry(a, b, c):
    while a > 0 or b > 0 or c > 0:
        number_sum = (a % 10) + (b % 10) + (c % 10)
        if number_sum >= 10:
            return True
            break
        else:
            a //= 10
            b //= 10
            c //= 10
        
sol = -1

for i in range(length - 2):
    for j in range(i + 1, length - 1):
        for k in range(j + 1, length):
            if is_carry(arr[i], arr[j], arr[k]):
                continue
            else:
                sol = max(sol, arr[i]+ arr[j]+ arr[k])

print(sol)
                


            








