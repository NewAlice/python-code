def main():
  try:
    #f=open('filex.txt')
    #f=open('file1.txt')
     f=open('file1.txt','rb')
     x=1/0
  except:
    print('unkown problem')
  except FileNotFoundError as e:
    print('problem is ', e)
  except ZeroDivisionError as e:
    print('a problem occured',e)
  print('all done!')



main()
