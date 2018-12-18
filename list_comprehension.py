"""
List comprehensions provide a concise way to create lists. 

It consists of brackets containing an expression followed by a for clause, then
zero or more for or if clauses. The expressions can be anything, meaning you can
put in all kinds of objects in lists.

The result will be a new list resulting from evaluating the expression in the
context of the for and if clauses which follow it. 

The list comprehension always returns a result list. 
"""

#Suppose, we want to separate the letters of the word human and add the letters as items of a list.


word = "human"

list1 = [letter for letter in word]
print(list1)

"""
If you noticed, human is a string, not a list. This is the power of list comprehension. 
It can identify when it receives a string or a tuple and work on it like a list.
"""



# Using Lambda functions inside List

lambda_func = lambda a: a

letters = list(map(lambda_func, word))
print(letters)


# Conditions in List Comprehension

new_list = [ i for i in range(0, 20) if i % 2 == 0] 

print(new_list)


# Nested IF with List Comprehension
"""
Here, list comprehension checks:

    Is y divisible by 3 or not?
    Is y divisible by 5 or not?

"""

new_list = [i for i in range(1, 100) if i % 3 == 0 if i % 5 == 0]

print(new_list)


#if...else With List Comprehension

list1 = [i if i % 2 ==0 else 'odd' for i in range(10)]

print(list1)


# Nested Loops in List Comprehension

matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
trans_matrix = []

for i in range(len(matrix[0])):
	transposed_row = []
	for row in matrix:
		transposed_row.append(row[i])
	trans_matrix.append(transposed_row)


print(trans_matrix)


trans_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print(trans_matrix)
