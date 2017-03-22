def main():
  try:
    fh=open('file1.txt')
    for line in fh: 
      print(line.strip())
  except IOError as e:
    print('could not open this file',e)
  #else:
  #  for line in fh: print(line.strip())

main()