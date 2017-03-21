import zipfile

fh = zipfile.ZipFile('mydata.zip','w')

fh.write('file1.txt')
fh.write('bigfile.txt')
#fh.write('bigfile.txt','newfile.txt','newbig.txt')

fh.close()