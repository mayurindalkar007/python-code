# Given array and their positions according to number of smaller digit
# on their left.
# Example
	# 8 2 4 3 6 1 5 7 
	# 0 0 1 1 3 0 3 6 // No element less than 2 on left of 2
#			  // 1 element less than 4 on left of 4 i.e 2
# input :-
	# Enter array:
	# 4 3 6 2 1 8 5 7
	# Enter position:
	# 1 1 3 0 0 0 3 6
# Output:-
	# Original array and postions are:-
	# 8 2 4 3 6 5 1 7
	# 0 0 1 1 3 3 0 6

class LL:
	def __init__(self, data, position):
		self.data = data
		self.position = position
		self.next = None

	@staticmethod
	def insert_tree(node, new_node):
		while(node.next != None):
			node = node.next
		node.next = new_node

	@staticmethod
	def insert_tree_others(node, new_node):
		pos = new_node.position
		prev = node
		while(pos):
			#print(node.data, new_node.data, pos)
			if node.data < new_node.data:
				pos -= 1
			prev = node
			node = node.next
		temp = prev.next
		prev.next = new_node
		new_node.next = temp

	@staticmethod
	def displsy(node):
		return_val = ''
		pos_val = ''
		while(node.next != None):
			return_val += str(node.data) + ' '
			pos_val += str(node.position) + ' '
			node = node.next
		return_val += str(node.data)
		pos_val += str(node.position)
		return (return_val,pos_val)

if __name__ == '__main__':
	heights = map(int, raw_input('Enter array:\n').strip().split())
	position = map(int, raw_input('Enter position:\n').strip().split())
	root = None

	dict1 = {}
	for i  in range(len(position)):
		try:
			dict1[position[i]].append(heights[i])
		except:
			dict1[position[i]] = [heights[i]]

	for i in sorted(dict1.keys()):
		if i == 0:
			for num in sorted(dict1[i], reverse=True):
				if root == None:
					root = LL(num, i)
				else:
					new_node = LL(num, i)
					LL.insert_tree(root, new_node)
		else:
			for num in sorted(dict1[i]):
				new_node = LL(num, i)
				LL.insert_tree_others(root, new_node)

	print('\nOriginal array and postions are:-')
	for ele in LL.displsy(root):
		print(ele)
