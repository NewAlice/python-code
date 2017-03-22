import operator

getseconditem = operator.itemgetter(1)

ls = ['a','b','c','d']

print(getseconditem(ls))

print(operator.itemgetter(1,3,5)('abcdefg'))