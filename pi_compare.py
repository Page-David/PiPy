#!/usr/bin/env python
# Compare calculating result with standard digits

def read_digits():
	with open("pi_digits") as f:
		return f.read()

def compare(cal_res):
	standard = read_digits()
	for i in range(len(cal_res)):
		if cal_res[i] != standard[i]:
			break
	return float(i+1) / len(cal_res), i - 1

if __name__ == "__main__":
	print compare('3.14')
