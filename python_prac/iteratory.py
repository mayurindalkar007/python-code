# iterator requiers 2 method __iter__ and __next__ 
# next = 2.7 and __next__ = python 3
# requires StopIteration exception to stop iteration



class mayur:
	def __init__(self, low, high):
		self.low = low
		self.high = high
	
	def __iter__(self):
		return self

	def next(self):
		if self.low > self.high:
			raise StopIteration

		temp = self.low
		self.low += 1
		return temp

#for i in range(0,5):
#	print(i)

m = mayur(0, 5)

# call iter over this object 

iteratr = iter(m)

print(next(iteratr))

#for i in m:
#	print(i)
