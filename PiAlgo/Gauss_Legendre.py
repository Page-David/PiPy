#!/usr/bin/env python
# Module used Gause Lagendre Algorithm to Calculate pi

from decimal import *
import pi_compare
import math
import time

def pi(digit):
	getcontext().prec = digit+1
	am, a, b, t, p = 0, 1, 1 / Decimal(2).sqrt(), 1 / Decimal(4), 1
	while am != a:
		am, bm, tm, pm = a, b, t, p
		a = Decimal((am+bm)/2)
		b = Decimal(am*bm).sqrt()
		t = Decimal(tm-pm*(am-a)**2)
		p = 2 * pm
	pi = Decimal((a+b) ** 2/(4*t))
	return str(pi)

if __name__ == "__main__":
	pi = pi(1000)
	print pi
	print pi_compare.compare(pi)
