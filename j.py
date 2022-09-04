a = int(input("첫 번째 과목의 점수를 입력하세요: "))
b = int(input("두 번째 과목의 점수를 입력하세요: "))
c = int(input("세 번째 과목의 점수를 입력하세요: "))

sum = a + b + c / 3

if (sum > 50) :
    print("평균 점수는 {0}으로 합격입니다.".format (sum))

else : print("평균 점수는 {0}으로 불합격입니다.".format (sum))
