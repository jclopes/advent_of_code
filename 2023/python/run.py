#! /bin/env python

import sys
import os.path

def main():
	"""Executes the code for the given day.
	Dinamically imports the module for the day we pass in the arguments.

	Example commandline execution:
	 > ./run.py ../input 2
	"""
	input_folder = sys.argv[1]
	day = sys.argv[2]
	if len(day) == 1: day = "0" + day

	input_file = os.path.join(input_folder, day + ".txt")

	module = __import__('d' + day)
	func = getattr(module, 'main')

	func(input_file)

if __name__ == '__main__':
	main()
