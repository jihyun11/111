from unittest import result


def getSum(num):
    result = 0
    for i in range (num+1):
        result += i
    return result
n = int(input("정수를 입력하세요: "))
sum = getSum(n)
print("0부터 {0}까지의 합계는 {1} 입니다.".format (n, sum))

def getSum(a, b):
    sum = a + b
    return sum
result = getSum(6, 5)
print(result)
