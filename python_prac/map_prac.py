#map() function returns a list of the results after applying the given function
#to each item of a given iterable (list, tuple etc.) 


# syntex - 
# map(fun, iter)


#Parameters :
#    fun : It is a function to which map passes each element of given iterable.
#    iter : It is a iterable which is to be mapped. 


#NOTE : You can pass one or more iterable to the map() function.


#Returns :
#     Returns a list of the results after applying the given function  
#     to each item of a given iterable (list, tuple etc.) 


def addition(n): 
    return n + n 
  
# We double all numbers using map() 
numbers = (1, 2, 3, 4) 
result = map(addition, numbers) 
print(result)


def map_wiht_dict(num):
	return num * num

dict1 = {'num1':1, 'num2':2}
result = map(map_wiht_dict, dict1.values())

print(result)


# map with lambda

list1 = [1, 2, 3, 4, 5]
result = map(lambda a:a*a*a , list1)

print(result)
