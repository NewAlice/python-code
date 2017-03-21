import codecs, encodings, sys

xmlfile=sys.argv[1]
fh = open(xmlfile)
counter=0
for line in fh:
  if(counter == 0):
    firstLine=line.split("\n")[0]
  counter+=1
  
print(firstLine)
if (firstLine.startswith("<?xml")):
  print("yes,this is an xml file")
else:
  print("No,this is not an xml file")
