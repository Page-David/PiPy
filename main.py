#!/usr/bin/env sage
import Gauss_Legendre
import reverse_tan
import pi_compare
import unbounded_spigot
import spigot
import time
from sage.all import *

class Analyser(object):
	
	def __init__(self, method_list):
		self.end = 1000
		self.start = 100
		self.step = 100
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
				print d, end_time, accuracy
			self.figure += list_plot(self.time_set, color = m.color, legend_label = m.name)
			self.figure2 += list_plot(self.accuracy_list, color = m.color, legend_label = m.name)
			self.time_set, self.accuracy_list = list(), list()
		self.figure.axes_labels(["$digits$", "$time$"])
		self.figure2.axes_labels(["$digits$", "$accurancy$"])
		save(self.figure.plot(), filename="time.svg")
		save(self.figure2.plot(), filename="accurancy.svg")

class Pi_Func(object):

	def __init__(self, name, color, function):
		self.name = name
		self.color = color
		self.function = function


if __name__ == "__main__":
	method_list = [
				Pi_Func("Gauss_Legendre", "red", Gauss_Legendre.pi),
				Pi_Func("Reverse_Tan", "blue", reverse_tan.pi),
				Pi_Func("Jeremy Gibbons's Unbounded Spigot", "green", unbounded_spigot.pi),
				Pi_Func("Stanley Rabinowitz and Stan Wagon's spigot algorithm", "orange", spigot.pi)
				]
	analyse = Analyser(method_list)
	analyse.run()
