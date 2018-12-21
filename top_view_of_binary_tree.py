class TopView:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	@staticmethod
	def inorder_traverse(node):
		if node.left:
			TopView.inorder_traverse(node.left)
		print(node.data)
		if node.right:
			TopView.inorder_traverse(node.right)

	@staticmethod
        def verticle_travers(node, level, level_dict):
		if node.left:
			TopView.verticle_travers(node.left, level - 1, level_dict)
		try:
			level_dict[level].append(node.data)
		except:
			level_dict[level] = [node.data]
		if node.right:
			TopView.verticle_travers(node.right, level + 1, level_dict)
		return level_dict


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

	#@staticmethod
	#def top_view(node):
		

			
			
			

if __name__ == '__main__':
	root = None
	while(True):
		choice = raw_input('Enter choice:\n1.Enter Tree\n2.Print Inorder\n3.Print Level traversle.\n4.Print top view of tree\n5.Exit\n')
		if choice == '1':
			tree = map(int, raw_input('Enter data:\n').strip().split())
			for dat in tree:
				new_node = TopView(dat)
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
			TopView.inorder_traverse(root)
		elif choice == '3':
			l_dict = TopView.level_travers(root)
			print(l_dict)
		elif choice == '4':
			l_order = TopView.level_travers(root)
			top_view = []
			print('\nLevel order traverse:-')
			print(l_order)
			v_dict = TopView.verticle_travers(root, 0, {})
			print('\nVertical order traverse:-')
			for key in sorted(v_dict.keys()):
				if len(v_dict[key]) == 1:
					top_view.append(v_dict[key][0])
				else:
					for i in range(len(l_order)):
						if l_order[i] in v_dict[key]:
							top_view.append(l_order[i])
							l_order.pop(i)
							break
				print(v_dict[key])
			print('\nTop View:-')
			print(top_view)
		elif choice == '5':
			break
