#!/usr/bin/python3
n = 0
while n < 100:
	if n == 99:
		print('{:d}'.format(n))
	else:
		print('{:02d}'.format(n), end=', ')
	n = n + 1
