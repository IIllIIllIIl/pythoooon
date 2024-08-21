def p (space, space_num, *args): #args = arguments
      str = args[0]
      for i in range(1, len(args)):
            str= str + (space * space_num) + args[i]
      print(str)

p(',', 3 ,  '👍','😁','💕','😊','😂','🤣')
