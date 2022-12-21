def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum

a = input("각 숫자를 공백으로 구분해 입력해 주세요: ")
b = a.split()
c = list(map(int, b))

max = -1
for x in c:
    temp = digit_sum(x)
    if temp > max:
        max = temp
        result = x

print(f"자릿수의 합이 가장 큰 수는 {result}입니다.")