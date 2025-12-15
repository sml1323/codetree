n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.


sorted_numbers = sorted(numbers, reverse=True)


# index dict
index_dict = {}
for i in sorted_numbers:
    a = numbers.index(i)
    index_dict[a] = i

max_idx = numbers.index(sorted_numbers[0])
next_idx = 0

for i, v in index_dict.items():
    if i != max_idx and abs(max_idx - i) > 1:
        next_idx = i
        break
print(index_dict[max_idx] + index_dict[next_idx])


