def main():

  buffersize=500000
  infile=open('bigfile.txt','r')
  outfile=open('newbig.txt','w')
  buffer=infile.read(buffersize)

  while len(buffer):
    outfile.write(buffer)
    print('.',end='')
    buffer=infile.read(buffersize)
  print()
  print('Done.')

main()