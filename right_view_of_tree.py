class right_view_of_tree:
	def __init__(self, root):
		self.data = data
		self.left = None
		self.right = None

	@staticmethod
	def _print_right_view(node, counter):
		arr[counter] = node.data
		if node.left != None:
			right_view_of_tree._print_right_view(node.left, counter + 1)
		if node.right != None:
			right_view_of_tree._print_right_view(node.right, counter + 1)

	@staticmethod
	def _insert_in_tree(node, data):
		new_node = right_view_of_tree(data)
		while(True):
			if data < node.data and node.left != None:
				node = node.left
			if data > node.data and node.right != None:
				node = node.right
			if data < node.data and node.left == None:
				node.left = new_node
				return 
			if data > node.data and node.right == None:
				node.right = new_node
				return

	@staticmethod
	def _print_inorder(node):
		if node.left != None:
			right_view_of_tree._print_inorder(node.left)
		print(node.data)
		if node.right != None:
			right_view_of_tree._print_inorder(node.right)
				

	
			
if __name__ == '__main__':
	root = None	
	arr = [0]*100
	while(True):
		choice = raw_input("Enter choice\n1.Enter data\n2.Print inorder\n3.Print right view\n4.Exit\n")
		if choice == '1':
			data = raw_input('\nEnter data:\n')
			if root == None:
				root = right_view_of_tree(data)
			else:
				right_view_of_tree._insert_in_tree(root, data)
		elif choice == '2':
			print('\nYour inorder:-\n')
			right_view_of_tree._print_inorder(root)
		elif choice == '3':
			print('\nYour right view:-\n')	
			right_view_of_tree._print_right_view(root, 0, arr)	
			for num in arr:
				if num != 0:
					print(num)
