def main():
  #f = open('bday.jpg','rb')
  #for line in f:
  #  print(line,end='')
  inputfile = open('bday.jpg','rb')
  outputfile = open('bday2.jpg','wb')

  buffersize=50000
  buffer=inputfile.read(buffersize)
  while len(buffer):
    outputfile.write(buffer)
    print('.',end='')
    buffer = inputfile.read(buffersize)
  print()
  print('Copy complete!')
main()