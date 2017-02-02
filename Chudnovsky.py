#!/usr/bin/env python

from mpmath import *
import pi_compare

def pi(digits):
	mp.dps = digits
	K, M, L, X, S = 6, mpf('1'), 13591409, 1, mpf('13591409')
	new_S = i = 0
	while new_S != S:
		new_S = S
		M = (K**3 - K*16) * M / (i+1)**3
		L += 545140134
		X *= -262537412640768000
		S += (M * L) / X
		K += 12
		i += 1
	return str(426880 * mpf('10005').sqrt() / S)

if __name__ == "__main__":
	P = pi(1000)
	print P
	print pi_compare.compare(str(P))
