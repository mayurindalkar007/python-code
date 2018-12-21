def star(func):
	def inner():
		print('*' * 30)
		func()
		print('*' * 30)
	return inner

def percent(func):
	def inner():
		print('%' * 30)
		func()
		print('%' * 30)

	return inner

#@percent
#@star
def func():
	print('Hi mayur')

func = star(func)
func = percent(func)
func()



