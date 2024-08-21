def sum(*numbers):
      sum_value = 0
      for i in numbers:
            sum_value = sum_value + i
      return sum_value

res = sum(1, 3, 5, 7, 9, 11)
print(res)
