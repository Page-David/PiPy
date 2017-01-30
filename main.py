#!/usr/bin/env sage
import Gauss_Legendre_mpmath
import reverse_tan
import reverse_tan_John_Machin
import pi_compare
import unbounded_spigot
import spigot
import Chudnovsky
import time
from sage.all import *
import sys

class Analyser(object):
	
	def __init__(self, method_list, last):
		self.end = int(last)
		self.start = 10
		self.step = 10
		self.time_set = list()
		self.accuracy_list = list()
		self.figure = point((0,0))
		self.figure2 = point((0,0))
		self.methods = method_list
	
	def run(self):
		for m in self.methods:
			for d in range(self.start, self.end, self.step):
				start_time = time.time()
				res = m.function(d)
				end_time = time.time() - start_time
				self.time_set.append((d, end_time))
				accuracy = pi_compare.compare(res)[0]
				self.accuracy_list.append(accuracy)
				print m.name, d, end_time, accuracy
				if end_time > 0.1: break
			self.figure += list_plot(self.time_set, color = m.color, legend_label = m.name)
			self.figure2 += list_plot(self.accuracy_list, color = m.color)
			self.time_set, self.accuracy_list = list(), list()
		self.figure.axes_labels(["$digits$", "$time$"])
		self.figure2.axes_labels(["$digits$", "$accurancy$"])
		save(self.figure.plot(), filename="time.svg", figsize=10, ymax=0.1, xmax=1000)
		save(self.figure2.plot(), filename="accurancy.svg", ymin=0.9, ymax=1.0)

class Pi_Func(object):

	def __init__(self, name, color, function):
		self.name = name
		self.color = color
		self.function = function


if __name__ == "__main__":
	method_list = [
				Pi_Func("Gauss_Legendre", "red", Gauss_Legendre_mpmath.pi),
				Pi_Func("Reverse_Tan", "blue", reverse_tan.pi),
				Pi_Func("Jeremy Gibbons's Unbounded Spigot", "green", unbounded_spigot.pi),
				Pi_Func("Stanley Rabinowitz and Stan Wagon's spigot algorithm", "orange", spigot.pi),
				Pi_Func("Chudnovsky algorithm", "black", Chudnovsky.pi),
				Pi_Func("Reverse_Tan_John_Machin", "yellow", reverse_tan_John_Machin.pi)
				]
	analyse = Analyser(method_list, sys.argv[1])
	analyse.run()
