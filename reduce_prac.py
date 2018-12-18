#The reduce(fun,seq) function is used to apply a particular function passed in its argument
#to all of the list elements mentioned in the sequence passed along.

"""	
Working : 

    - At first step, first two elements of sequence are picked and the result is obtained.
    - Next step is to apply the same function to the previously attained result and the number 
      just succeeding the second element and the result is again stored.
    - This process continues till no more elements are left in the container.
    - The final returned result is returned and printed on console

"""


def add_fuc(a, b):
	return a+b


list1 = [1, 2, 3, 4, 5]


result = reduce(add_fuc, list1)

print(result)

# Reduce with lamda -------------------->


result = reduce(lambda a,b:a+b, list1)
print(result)
