class files:
  def __init__(self,ftype='text'):
    self._ftype='text'
  def move(self):
    print("file is moving")
  def copy(self):
    print("file is being copied")
  def delete(self):
    print("file is being removed")

  def set_ftype(self,ftype):
    self._ftype=ftype

  def get_ftype(self):
    return self._ftype

def main():
  execs=files()
  execs.move()
  execs.copy()
  print(execs.get_ftype())

  execs.set_ftype('mov')
  print(execs.get_ftype())

main()