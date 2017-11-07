import sys
reload(sys)
sys.setdefaultencoding('utf8')



fw=open('data.txt',w)

for x in xrange(1,18):
    fw.write(str(x))
fw.close()

a='Hello World'
print(a)
