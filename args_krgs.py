def func1_args(*args):
	print('in function')
	print(func1_args.__name__)
	for ar in args:
		print(ar)

func1_args()
print('================================================')
func1_args('mayur', 'indalkar')
print('================================================')


def func2_kwargs(**kwars):
	print('in function {}'.format(func2_kwargs.__name__))
	print(kwars.items())


func2_kwargs()

print('================================================')

func2_kwargs(name='mayur', lastname='indalkar')	

print('================================================')


def func3_args_kwargs(*args, **kwars):
	print('in function {}'.format(func3_args_kwargs.__name__))
	for ar in args:
		print(ar)

	print(kwars.items())


func3_args_kwargs('veritas', 'access', name='mayur', lastname='indalkar')
