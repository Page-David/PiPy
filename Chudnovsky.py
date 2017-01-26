#!/usr/bin/env python

from mpmath import *
import pi_compare

mp.dps = 1000
def pi():
	K, M, L, X, S = 6, mpf('1'), 13591409, 1, mpf('13591409')
	for i in xrange(0,100):
		M = (K**3 - K*16) * M / K**3
		L += 545140134
		X *= -262537412640768000
		S += (M * L) / X
		K += 12
	return mpf('426880') * mpf('10005').sqrt() / S

P = pi()
print P
print pi_compare.compare(str(P))
