#!usr/bin/env python
# encoding:utf-8

SYMBOLS = {'}':'{', ']':'[', ')':'(', '>':'<' }
SYMBOLS_L, SYMBOLS_R = SYMBOLS.values(), SYMBOLS.keys()

def check(s):
	''''''
	括号匹配
	''''''
	arr = []
	for c in s:
		if c in SYMBOLS_L:
			arr.append(c)
		elif c in SYMBOLS_R:
			if arr and arr[-1] == SYMBOLS[c]:
				arr.pop()
			else:
			 return FALSE
	return True

print(check("3*{3+[(2-3)*(4+5)]}"))
print(check("3*{3+[4-6}]"))