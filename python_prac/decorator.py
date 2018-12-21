


def decorator(func):
	def inner_func(name):
		print('Name passed is {}'.format(name))
		func(name)
	return inner_func

@decorator  # this actuall means say_hi_to = decorator(say_hi_to)
def say_hi_to(name):
	print('Hi {}'.format(name))


say_hi_to('mayur')
