import math

class prime:
	def __init__(self, maxx):
		self.a = 1
		self.maxx = maxx
	def __iter__(self):
		return self

	def next(self):
		self.a += 1
		if self.a > self.maxx:
			 raise StopIteration
		elif prime.is_prime(self.a):
			return self.a
		else:
			return self.next()
	@staticmethod
	def is_prime(num):
		for i in range(2, int(math.sqrt(num)) + 1):
			if num % i == 0:
				return False
		return True


def prime_using_genrator(num):
	a = 1
	while (a < num):
		a += 1
		if prime.is_prime(a):
			yield a


num = int(raw_input('Enter number:\n'))
p = prime(num)


for i in p:
	print(i)

#==========================================================================================
gen = prime_using_genrator(num)

for i in gen:
	print(i)
