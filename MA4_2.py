#!/usr/bin/env python3

from integer import Integer
from time import perf_counter as pc

#def fib_py(n):
	#if n <= 1:
		#return n
	#else:
		#return (fib_py(n-1) + fib_py(n-2))

def main():
	f = Integer(5)
	print(f.get())
	f.set(7)
	print(f.get())

	#start1 = pc()
	#f.fib_py()
	#print(f.fib_py())
	#end1 = pc()

	#print(f"fib python took {round(end1-start1, 2)} seconds")

	start2 = pc()
	f.fib_cpp()
	print(f.fib_cpp())
	end2 = pc()

	print(f"fib c++ took {round(end2-start2, 2)} seconds")

if __name__ == '__main__':
	main()
