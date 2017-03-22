class inclusive_range:
  def __init__(self,*args):
      numargs=len(args)
      if numargs < 1:
        raise TypeError('requires at least 1 paramter')
      elif numargs == 1:
        self.stop=args[0]
        self.step = 1
        self.start=0
      elif numargs == 2:
        (self.start,self.stop) = args
        self.step=1
      elif numargs == 3:
        (self.start,self.stop,self.step) = args
      else:
        raise TypeError('expected at most 3 param received {}'.format(numargs))
  
  def __iter__(self):
    i = self.start
    while i<=self.stop:
      yield i
      i +=self.step

     


def main():
  #o = range(25)
  #o = inclusive_range(25)
  #o = range(5,25,2)
  o = inclusive_range(5,25,2)
  for i in o: print(i, end=' ')

main()