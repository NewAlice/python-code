with open('../file1.txt') as fh:
  for line in iter(fh.readline, ''):
    print(line)

fhindle=open('../file1.txt')

for line in fhindle:
  #print(line)
  #print(line.split())
  print(line.split("\n")[0])