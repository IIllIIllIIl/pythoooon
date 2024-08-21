b=[]
def fn(a,b=[]):
      b.append(a)
      print(b)

fn(3)
fn(6)
fn(10)
print(b)