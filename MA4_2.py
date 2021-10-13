#!/usr/bin/env python3

from integer import Integer
from time import perf_counter as pc

def fib_py(n):
	if n <= 1:
		return n
	else:
		return (fib_py(n-1) + fib_py(n-2))

def main():
	f = Integer(5)
	print(f.get())
	f.set(47)
	print(f.get())

	start1 = pc()
	resultpy = fib_py(47)
	print(resultpy)
	end1 = pc()

	print(f"fib python took {round(end1-start1, 5)} seconds")#Took approx 27.5 minutes

	start2 = pc()
	resultcpp = f.fib_cpp()
	print(resultcpp)
	end2 = pc()

	print(f"fib c++ took {round(end2-start2, 5)} seconds")#Took approx 1 minute

if __name__ == '__main__':
	main()
