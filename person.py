""" Python interface to the C++ Person class """
import ctypes
from numba import njit
from time import perf_counter as pc
import matplotlib.pyplot as plt
lib = ctypes.cdll.LoadLibrary('./libperson.so')

class Person(object):
	def __init__(self, age):
		lib.Person_new.argtypes = [ctypes.c_int]
		lib.Person_new.restype = ctypes.c_void_p
		lib.Person_get.argtypes = [ctypes.c_void_p]
		lib.Person_get.restype = ctypes.c_int
		lib.Person_set.argtypes = [ctypes.c_void_p,ctypes.c_int]
		lib.Person_fib.argtypes = [ctypes.c_void_p]
		lib.Person_fib.restypes = ctypes.c_int
		lib.Person_delete.argtypes = [ctypes.c_void_p]
		self.obj = lib.Person_new(age)

	def get(self):
		return lib.Person_get(self.obj)

	def set(self, age):
		lib.Person_set(self.obj, age)
        
	def __del__(self):
		return lib.Person_delete(self.obj)
	def fib(self):
		return lib.Person_fib(self.obj)
#@njit
def fib_py(n):
	if  n<=1:
		return 1
	else:
		return fib_py(n-1) + fib_py(n-2)
cpp_time =[]
numba_time = []

for n in range(30,45):
	print(n)
	start = pc()
	f = Person(n)
	f.fib()
	end = pc()
	cpp_time.append(end-start)
	start = pc()
	fib_py(n)
	end = pc()
	numba_time.append(end-start)


plt.plot(range(30,45), numba_time)
plt.plot(range(30,45), cpp_time)
plt.savefig('firsttestplot.png')
print(cpp_time)
print(numba_time)

