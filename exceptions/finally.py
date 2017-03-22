def main():

  counter=0
  try:
    fh=open("xfile1.txt")
    for line in fh: print(line.strip())
  except:
    counter+=1
    #print('there was an error')
    pass
  finally:
    print()
    print("there were %d errors in ther process" %counter)
    print('all work was done')

main()