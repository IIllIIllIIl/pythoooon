import random #모듈 <- 함수들 모음
result='my_number:'
for i in range(5): #0~5까지 6번 반복실행 
    num=random.randint(1,6) #1~46의 범위에서 임의의 정수값 1개 저장
    result = f" {i}:{num}"
    print(result)
