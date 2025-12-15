n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.


sol = 0
for i in range(len(numbers)):
    first_max = numbers[i]
    f_idx = i
    second_max = 0
    for j in range(len(numbers)):
        if abs(f_idx - j) > 1:
            second_max = max(second_max, numbers[j])
    sum_of_two = first_max + second_max
    sol = max(sol, sum_of_two)



print(sol)



