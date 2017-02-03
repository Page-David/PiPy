#!/usr/bin/env sage
from PiAlgo import *
import time
from sage.all import *
import argparse

class Analyser(object):
	
	def __init__(self, method_list, last, max_time):
		self.end = last
		self.start = 10
		self.step = 10
		self.time_set = list()
		self.accuracy_list = list()
		self.figure = point((0,0))
		self.figure2 = point((0,0))
		self.methods = method_list
		self.max_time = max_time
	
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
				if end_time > self.max_time: break
			self.figure += list_plot(self.time_set, color = m.color, legend_label = m.name)
			self.figure2 += list_plot(self.accuracy_list, color = m.color)
			self.time_set, self.accuracy_list = list(), list()
		self.figure.axes_labels(["$digits$", "$time$"])
		self.figure2.axes_labels(["$digits$", "$accurancy$"])
		save(self.figure.plot(), filename="time.svg", figsize=10, ymax=self.max_time, xmax=self.end)
		save(self.figure2.plot(), filename="accurancy.svg", ymin=0.9, ymax=1.0)

class Pi_Func(object):

	def __init__(self, name, color, function):
		self.name = name
		self.color = color
		self.function = function


if __name__ == "__main__":
	# config differet algorithms
	method_list = [
				Pi_Func("Gauss_Legendre", "red", Gauss_Legendre_mpmath.pi),
				Pi_Func("Reverse_Tan", "blue", reverse_tan.pi),
				Pi_Func("Jeremy Gibbons's Unbounded Spigot", "green", unbounded_spigot.pi),
				Pi_Func("Stanley Rabinowitz and Stan Wagon's spigot algorithm", "orange", spigot.pi),
				Pi_Func("Chudnovsky algorithm", "black", Chudnovsky.pi),
				Pi_Func("Reverse_Tan_John_Machin", "yellow", reverse_tan_John_Machin.pi),
				Pi_Func("Reverse_Tan_Euler", "dodgerblue", reverse_tan_Euler.pi)
				]
	# config user parser
	parser = argparse.ArgumentParser(description = 'Calculate pi to thousands of digits')
	parser.add_argument('digits', metavar='digits',
	type=int, help='how many digits of pi you need')
	parser.add_argument('--max-time', default=0.1,
	dest='second', help='process will stop when algo takes more time to finish (default: 0.1)')
	args = parser.parse_args()
	
	# START
	analyse = Analyser(method_list, args.digits,
	args.second)
	analyse.run()
