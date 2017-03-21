import zipfile

fh = zipfile.ZipFile('mydata.zip','r')

names=fh.namelist()

for name in names:
  print('processing %s' %name)
  fh2=fh.open(name)
  contents=fh2.read()
