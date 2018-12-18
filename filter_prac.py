# The filter() method filters the given sequence with the help of a function 
# that tests each element in the sequence to be true or not.

"""
filter(function, sequence)

Parameters:
	function: function that tests if each element of a 
		   sequence true or not.
	sequence: sequence which needs to be filtered, it can 
	       	   be sets, lists, tuples, or containers of any iterators.

Retruns:
returns an iterator that is already filtered.
"""


# function that filters vowels 
def fun(variable): 
    letters = ['a', 'e', 'i', 'o', 'u'] 
    if (variable in letters): 
        return True
    else: 
        return False
  
  
# sequence 
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r'] 
  
# using filter function 
filtered = filter(fun, sequence) 

print(set(filtered))


# Filter with lamda
result = filter(lambda a: True if a in ['a', 'e', 'i', 'o', 'u'] else False, sequence)

print(result)
