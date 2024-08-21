import random
numbers=[]#나온 숫자를 기억하기 위한 빈 list
result="my numbers: "
cnt=0 #cnt의 초기값
while cnt<6: #몇번 반복할지 모를때 while문 
    num=random.randint(1,46)
    if num not in numbers: #중복 되지 않은 숫자가 나왔을때
        numbers.append(num)#list에 요소 추가
        result=result+f" {num}"
        cnt=cnt+1     
print(result)
