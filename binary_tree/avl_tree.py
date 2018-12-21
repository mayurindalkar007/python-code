class avl:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	@staticmethod
	def insert_in_tree(root, data):
		node = root
		new_node = avl(data)
		while(True):
			if data < node.data and node.left != None:
				node = node.left
			if data > node.data and node.right != None:
				node = node.right
			if data < node.data and node.left == None:
				node.left = new_node
				break
			if data > node.data and node.right == None:
				node.right = new_node
				break

	@staticmethod
	def print_inorder(node):
		if node.left != None:
			avl.print_inorder(node.left)
		print(node.data)
		if node.right != None:
			avl.print_inorder(node.right)

	@staticmethod
	def find_minimum_in_subtree(node):
		while(node.left != None):
			node = node.left
		return node.data

	@staticmethod
	def delete_node(node, data, parent = None):
		if data == node.data:
			if node.left != None and node.right != None:
				minimum_vale = avl.find_minimum_in_subtree(node.right)
				node.data = minimum_vale
				avl.delete_node(node.right, node.data, node)
			elif node.left == None and node.right == None:
				if parent.right != None and parent.right.data == data:
					parent.right = None
				if parent.left != None and parent.left.data == data:
					parent.left = None

			elif node.left == None and node.right != None:
				node.data = node.right.data
				avl.delete_node(node.right, node.data, node)
			elif node.left != None and node.right == None:
				node.data = node.left.data
				avl.delete_node(node.left, node.data, node)
			
			return True
		else:	
			if node.left != None and data < node.data:
				avl.delete_node(node.left, data, node)
			if node.right != None and data > node.data:
				avl.delete_node(node.right, data, node)

	@staticmethod
	def node_height(node):
		if node == None:
			return 0
		return (max(avl.node_height(node.left), avl.node_height(node.right)) + 1)

	@staticmethod
	def calculate_balance_factor(node):
		if node.left != None:
			avl.calculate_balance_factor(node.left)
		print (str(node.data) + "==>" + str(avl.node_height(node.left) - avl.node_height(node.right)))
		if node.right != None:
			avl.calculate_balance_factor(node.right)
		
if __name__ == "__main__":
	root = None
	while(True):
		print("\nEnter Choice\n1.Insert node.\n2.Delete Node\n3.Print inorder\n4.Calculate height of each node.\n5.Exit\n")
		choice = raw_input()
		if choice == '1':
			print("Enter Data")
			data = raw_input()
			if root == None:
				root = avl(data)
			else:
				avl.insert_in_tree(root, data)
		elif choice == '2':
			print("Enter data to be deleted")
			data = raw_input()
			if root == None:
				print("Empty tree\n")
			elif data == root.data:
				root = None
			else:
				if avl.delete_node(root, data):
					print("Data deleted successfully")	
				else:
					print("Data not found in tree")
		elif choice == '3':
			if root == None:
				print("Empty tree\n")
			else:
				print("Inorder traversal-->\n")
				avl.print_inorder(root)
		elif choice == '4':
			if root == None:
				print("Empty tree\n")
			else:
				print("Node balance factor --->\n")
				avl.calculate_balance_factor(root)
		elif choice == '5':
			print("\nBye\n")
			break;
		else:
			print("\nWrong entry\n")

