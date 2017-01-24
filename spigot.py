#!/usr/bin/env python
def pi(digits):
	res = ""
	N,predig,nines = digits,-1,0
	len = 10*N/3
	a = [2]*len
	while N > 0:
		q = 0
		a = list(map(lambda x: 10*x,a))
		for i in range(len-1,0,-1):
			a[i] += q*(i+1)
			q = a[i]/(2*i+1)
			a[i] %= (2*i+1)
		a[0] += q
		q, a[0] = a[0]/10, a[0]%10
		if q == 9:
			nines +=1
		elif q == 10:
			res += str(predig+1)
			while nines > 0:
				res += str(0)
				nines -= 1
			predig = 0
		else:
			if predig != -1: res += str(predig)
			predig = q
			while nines > 0:
				res += str(9)
				nines -= 1
		N -= 1
	res += str(predig)
	return res[:1] + '.' + res[1:]

if __name__ == "__main__":
	print pi(100)
