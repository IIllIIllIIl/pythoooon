def min (*numbers):
      min_value = numbers[0]
      max_value = numbers[0]
      for number in numbers:
            if min_value>number:
                  min_value = number
            if max_value<number:
                  min_value = number
      return min_value, max_value
result=min(111,22,3,4,53)
print(result)
a, b= min(32,451,323 ,5,4, 213, 2321)
print("최솟값:", a)
print("최댓값", b)