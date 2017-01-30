#!/usr/bin/env python
from mpmath import *

def pi(digit):
	mp.dps = digit
	#pi = 4*(12*atan(1/mpf('49')) + 32*atan(1/mpf('57')) - 5*atan(1/mpf('239')) + 12*atan(1/mpf('110443')))
	pi = 4 * atan(1/mpf('2')) + 4 * atan(1 / mpf('3'))
	return str(pi)


