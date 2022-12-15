def getSum(num) :
    result = 0
    for i in range (num + 1):
        result += i
        return result



n = int(input("정수를 입력하세요:"))
sum = getSum(n)
print("0부터", n, "까지의 합계는", sum, "입니다.")


