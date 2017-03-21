def main():
	
	f = open('file1.txt','r')
	for line in f.readlines():
	  print(line,end='')
main()