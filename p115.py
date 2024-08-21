def star(letter, *args):
      for i in args:
            print(letter * i)

star("👌", 3)
star("😁",1,2,3)