class VerticleTraverse:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	@staticmethod
	def inorder_traverse(node):
		if node.left:
			VerticleTraverse.inorder_traverse(node.left)
		print(node.data)
		if node.right:
			VerticleTraverse.inorder_traverse(node.right)

	@staticmethod
	def verticle_travers(node, level, level_dict):
		if node.left:
			VerticleTraverse.verticle_travers(node.left, level - 1, level_dict)
		try:
			level_dict[level].append(node.data)
			#print(level_dict)
		except:
			level_dict[level] = [node.data]
		if node.right:
			VerticleTraverse.verticle_travers(node.right, level + 1, level_dict)
		return level_dict
			
			
			

if __name__ == '__main__':
	root = None
	while(True):
		choice = raw_input('Enter choice:\n1.Enter Tree\n2.Print Inorder\n3.Print Verticle traversle.\n4.Exit\n')
		if choice == '1':
			tree = map(int, raw_input('Enter data:\n').strip().split())
			for dat in tree:
				new_node = VerticleTraverse(dat)
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
			VerticleTraverse.inorder_traverse(root)
		elif choice == '3':
			l_dict = VerticleTraverse.verticle_travers(root, 0, {})
			print(l_dict)
			for key in sorted(l_dict.keys()):
				print(l_dict[key])
			
		elif choice == '4':
			break
