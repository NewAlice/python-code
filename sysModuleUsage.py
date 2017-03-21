import sys
def main():

  counter=0
  try:
    #fh=open("mydata.txt")
    fh=open("file1.txt")
  except:
    counter+=1
    pass
  finally:
    sys.exit("there were %d errors" %counter)

main()