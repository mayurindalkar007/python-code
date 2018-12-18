class with_statement:
	def __enter__(self):
		print('enter called')
		return 2
	def __exit__(self, type, value, traceback):
		print(type, value, traceback)
		print('exit block is called')
		return(isinstance(value, TypeError)) # This will handle TypeError exception, but all other exceptions will be raised

obj = with_statement() 

with obj as val:
	print('in code block')
	print(val)
	raise TypeError
