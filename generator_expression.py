
def simple_gen_expr():
	my_gen = ('hello' for i in range(3))
	print(my_gen)
	print(next(my_gen))
	print(next(my_gen))
	print(next(my_gen))
	try:
		print(next(my_gen))
	except Exception as e:
		print(dir(e))
		print(e.message)

	squars = (x*x for x in range(5))
	print(list(squars))

def gen_expr_with_filter():
	even_squars = (x*x for x in range(5) if x % 2 ==0)
	print(next(even_squars))
	print(next(even_squars))

	even_squars_odd_cube = (x*x if x % 2 ==0 else x*x*x for x in range(5))
	print(next(even_squars_odd_cube))
	print(next(even_squars_odd_cube))
	print(next(even_squars_odd_cube))
	print(next(even_squars_odd_cube))
	print(next(even_squars_odd_cube))

if __name__ == '__main__':
	simple_gen_expr()
	gen_expr_with_filter()	
