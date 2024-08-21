import random
def rolling_dice(pip, repeat):
      for i in range(repeat):           #함수 정의, 매개변수
            n = random.randint(1, pip)
            print("결과 : ", n)
            print(i, n)

#함수 호출
rolling_dice(6, 5)    #인수, 인자
