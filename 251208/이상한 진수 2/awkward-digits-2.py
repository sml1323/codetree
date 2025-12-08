a = input()

# Please write your code here.


# 앞의 자릿수부터 0 -> 1로 바꿈, 안된다면 그대로 10진수 변환하여 출력

new_number = list(a)
changed = False
a_len = len(a)
for i in range(len(new_number)):
    if new_number[i] == '0':
        new_number[i] = '1'
        changed = True
        break
    
if not changed:
    new_number[-1] = "0"
num = 0
for i in range(len(new_number)):
    num = num * 2 + int(new_number[i])



print(num)