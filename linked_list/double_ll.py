class double_ll:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

	@staticmethod
	def print_dll(node):
		if node == None:
			print("Empty DLL")
			return
		dll_str = ''
		while node.next != None:
			dll_str = dll_str + str(node.data) + "<--->"
			node = node.next
		dll_str = dll_str + str(node.data)
		print(dll_str)

	@staticmethod
	def print_reverse_dll(node):
		if node == None:
			print("Empty DLL")
			return
		dll_str = ''
		while node.prev != None:
			dll_str = dll_str + str(node.data) + "<--->"
			node = node.prev
		dll_str = dll_str + str(node.data)
		print(dll_str)
			

if __name__ == "__main__":
	head = None
	tail = None
	while True:
		choice = raw_input("Do you want to continue:\n")
		if choice == 'y':
			dat = raw_input("Enter element:\n")
			if head == None:
				head = double_ll(dat)
				continue

			new_node = double_ll(dat)
			node = head
			while(node.next != None):
				node = node.next
			node.next = new_node
			new_node.prev = node
			tail = new_node
		else:
			print("Double LL-->")
			double_ll.print_dll(head)
			print("Reverse DLL--->")
			double_ll.print_reverse_dll(tail)
			break
