s = input("enter a string:  ")
try:
	print(s[2], s[-2], s[:6], s[0:-2], s[1::2], s[1::2], s[::-1], s[-1::2], len(s), sep='\n')
except IndexError:
	print ('Error')