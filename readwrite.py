def main():
 
  f=open('file1.txt','r')
  #for line in f: print(line.split())
  #for line in f: print(line,end='')
  infile=open('file1.txt','r')
  outfile=open('newfile.txt','w')
  for line in infile:
    print(line,file=outfile,end='')
  print('Completed writing to newfile')
main()