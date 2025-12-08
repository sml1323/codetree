a = input()

# Please write your code here.


# 앞의 자릿수부터 0 -> 1로 바꿈, 안된다면 그대로 10진수 변환하여 출력

new_number = []
count = 0
for number in a:

    if number == "0" and count < 1:
        new_number.append("1")
        count += 1
    else:
        new_number.append(number)

num = 0
for i in range(len(new_number)):
    num = num * 2 + int(new_number[i])
print(num)