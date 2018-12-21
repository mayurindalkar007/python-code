class LevelOrderTraverse:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	@staticmethod
	def inorder_traverse(node):
		if node.left:
			LevelOrderTraverse.inorder_traverse(node.left)
		print(node.data)
		if node.right:
			LevelOrderTraverse.inorder_traverse(node.right)

	@staticmethod
	def level_travers(node):
		queue = []
		level = []
		queue.append(node)
		while queue:
			node = queue.pop(0)
			level.append(node.data)
			
			
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
		return level
			
			
			

if __name__ == '__main__':
	root = None
	while(True):
		choice = raw_input('Enter choice:\n1.Enter Tree\n2.Print Inorder\n3.Print Level traversle.\n4.Exit\n')
		if choice == '1':
			tree = map(int, raw_input('Enter data:\n').strip().split())
			for dat in tree:
				new_node = LevelOrderTraverse(dat)
				if root == None:
					root = new_node
				else:
					node = root
					while True:
						if dat <= node.data and node.left != None:
							node = node.left
						if dat > node.data and node.right != None:
							node = node.right
						if dat <= node.data and node.left == None:
							node.left = new_node
							break
						if dat > node.data and node.right == None:
							node.right = new_node
							break

		elif choice == '2':
			#print(root.data)
			LevelOrderTraverse.inorder_traverse(root)
		elif choice == '3':
			l_dict = LevelOrderTraverse.level_travers(root)
			print(l_dict)
			
		elif choice == '4':
			break
