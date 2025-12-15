n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.


first_max = max(numbers)
f_idx = numbers.index(first_max)
second_max = 0

for i in range(len(numbers)):
    if abs(f_idx - i) > 1:
        second_max = max(second_max, numbers[i])

print(first_max + second_max)


