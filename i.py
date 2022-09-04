birth = int(input("생일을 입력해 주세요!: "))
year = birth //10000
month = (birth % 10000) // 100
day = birth % 100

print("{0}년 {1}월 {2}일 생이네요!".format (year, month, day))

#i = int(input("생일을 입력해 주세요: "))
#j = int(input("생일을 입력해 주세요: "))
#h = int(input("생일을 입력해 주세요: "))
#print("{0}년 {1}월 {2}일 생이네요!".format (i, j, h))
