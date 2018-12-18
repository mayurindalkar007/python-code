class trie:
	def __init__(self, char):
		self.char = char
		self.children = []
		self.counter = 1
		self.endofword = False

	@staticmethod
	def insert_int_trie(node, word):
		for char in word:
			found_in_child = False
			for child in node.children:
				if child.char == char:
					child.counter += 1
					node = child
					found_in_child = True
					break
			if not found_in_child:
				new_node = trie(char)
				node.children.append(new_node)
				node = new_node

		node.endofword = True


	@staticmethod
	def find_word_in_trie(node, word):
		for char in word:
			char_found = False
			for child in node.children:
				if child.char == char:
					node = child
					char_found = True
					break
			if not char_found:
				return False

		if node.endofword:
			return True
		return False

	@staticmethod
	def find_prefix_in_trie(node, prefix):
		if not node.children:
			return (False, 0)
		for char in prefix:
			found_char = False
			for child in node.children:
				if child.char == char:
					found_char = True
					node = child
					break
			if not found_char:
				return (False, 0)
		return (True, node.counter)
		
				
if __name__ == "__main__":

	root = trie('*')
	while(True):
		print("Enter Choice:\n1.Insert Word\n2.Search Word\n3.Search Prefix\n4.Exit\n")
		choice = raw_input()
		if choice == '1':
			print("Enter word to be insert\n")
			word = raw_input()
			trie.insert_int_trie(root, word)
		elif choice == '2':
			print("Enter word to be search\n")
			word = raw_input()
			if trie.find_word_in_trie(root, word):
				print("Character Exist in trie\n")
			else:
				print("Character does not Exist in trie\n")
		elif choice == '3':
			print("Enter Prefix\n")
			prefix = raw_input()
			output = trie.find_prefix_in_trie(root, prefix)
			if output[0]:
				print("Prefix exist in trie for "+ str(output[1]) + "number of times\n")
			else:
				print("Prefix does not exist in trie\n")
			
		elif choice == '4':
			print("Bye\n")
			break
		else:
			print("Wrong Input\n")
		
