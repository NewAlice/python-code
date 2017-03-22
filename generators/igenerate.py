def main():

  print("this is a simple generator function")
  #for i in range(25):
  for i in inclusive_range(0,25,1):
    print(i,end=' ')

def inclusive_range(start,stop,step):
  i = start
  while i<stop:
    yield i
   # return i
    i+=step
main()