

class String():
	def __init__(self, str1):
		self.string = str1

	def __repr__(self):
		return ('this is object')

	def __add__(self, str2):
		return self.string + str2

def example1():
	str_obj = String('Hello')

	print(str_obj)
	print(dir(str_obj))


# Lets see working of add
def example2():
	str1 = String('mayur')
	str2 = 'Indalkar'
	print(type(str1), type(str2))
	str3 = str1 + str2 # will be executed as str3 = str1.__add__(str2) 

	print(str3)

if __name__ == '__main__':
	example2()
	
