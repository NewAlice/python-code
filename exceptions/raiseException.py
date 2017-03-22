def main():
  try:
    #fh = open('file1.txt')
    for line in readfile('filex.txt'): print(line.strip())
  except IOError as e:
    print('cannot read file: ', e)
 
def readfile(filename):
  fh = open(filename)
  return fh.readlines()
 
main()