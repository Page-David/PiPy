#!/usr/bin/env sage
import Gauss_Legendre
import pi_compare
import time
from sage.all import *

class Analyser(object):
	
	def __init__(self, method_list):
		self.end = 1000
		self.start = 100
		self.step = 100
		self.time_set = list()
		self.figure = point((0,0))
		self.figure2 = None
		self.methods = method_list
	
	def run(self):
		for m in self.methods:
			for d in range(self.start, self.end, self.step):
				start_time = time.time()
				m.function(d)
				end_time = time.time() - start_time
				self.time_set.append((d, end_time))
				print d, end_time
			self.figure += list_plot(self.time_set, color = m.color, legend_label = m.name)
		save(self.figure.plot(), filename="time.svg")

class Pi_Func(object):

	def __init__(self, name, color, function):
		self.name = name
		self.color = color
		self.function = function


if __name__ == "__main__":
	method_list = [Pi_Func("Gauss_Legendre", "red", Gauss_Legendre.pi)]
	analyse = Analyser(method_list)
	analyse.run()
