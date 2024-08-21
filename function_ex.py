list =['d', 'c', 'a', 'b']
list.reverse() #리스트 항목 순서 뒤집기
print(list)  
list.sort() #리스트 항목 정렬하기
print(list)
list.sort(reverse=True) #리스트 항목 역정렬하기
print(list)
for index, value in enumerate(list):
      print(index) #인덱스 번호
      print(value) #인덱스 번호에 할당된 문자