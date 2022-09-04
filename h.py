a = int(input("키를 입력하세요: "))
b = int(input("몸무게를 입력하세요: "))

c = a / (b * b)

if (c > 25) : print("BMI 지수가 {0} 이므로 비만입니다.".format(c))
elif (23 <= c < 25) : print("BMI 지수가 {0} 이므로 비만입니다.".format(c))
elif (18.5 <= c < 23) : print("BMI 지수가 {0} 이므로 비만입니다.".format(c))
else : print("BMI 지수가 {0}이므로 저체중입니다.".format(c))