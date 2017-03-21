try:
  fh=open('filename')
except IOError as e:
  if(e):   
    print(e)
  else:
    for l in fh:print()