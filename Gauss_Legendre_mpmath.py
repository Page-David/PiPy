#!/usr/bin/env python
# Module used Gause Lagendre Algorithm to Calculate pi

from mpmath import *

def pi(digit):
	mp.dps = digit+1
	am, a, b, t, p = 0, 1, 1 / mpf('2').sqrt(), 1 / mpf('4'), 1
	while am != a:
		am, bm, tm, pm = a, b, t, p
		a = (am + bm) / 2
		b = (am * bm).sqrt()
		t = tm-pm*(am-a)**2
		p = 2 * pm
		pi = (a+b) ** 2/(4*t)
	return str(pi)

if __name__ == "__main__":
	print(pi(100))
	
