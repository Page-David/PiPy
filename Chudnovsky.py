#!/usr/bin/env python

from mpmath import *
import pi_compare

def pi(digits):
	mp.dps = digits
	K, M, L, X, S = 6, mpf('1'), 13591409, 1, mpf('13591409')
	new_S = S
	for i in xrange(0,1000000):
		M = (K**3 - K*16) * M / (i+1)**3
		L += 545140134
		X *= -262537412640768000
		new_S += (M * L) / X
		K += 12
		if new_S == S:
			break
		else:
			S = new_S
	return str(426880 * mpf('10005').sqrt() / S)

if __name__ == "__main__":
	P = pi()
	print P
	print pi_compare.compare(str(P))
