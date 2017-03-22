def main():
  try:
   # fh=open("file1.txt")
    fh=open("xfile1.txt")
    print('file has been opened')
    print()
    for line in fh: print(line.strip())
  #except FileNotFoundError as e:
  #  print('error wsa ',e)
  except:
    pass
main()