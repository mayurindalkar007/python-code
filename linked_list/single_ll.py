class single_ll:
	def __init__(self, content):
		self.data = content
		self.next = None

	@staticmethod
	def print_ll(node):
		if node == None:
			print("Empty LL")
			return
		ll_str = ''
		while(node.next != None):
			ll_str = ll_str + str(node.data) + "--->"
			node = node.next
		ll_str = ll_str + str(node.data)
		print(ll_str)

	@staticmethod
	def print_ll_using_rec(node):
		if node != None:
			print(node.data)
			single_ll.print_ll_using_rec(node.next)

if __name__ == "__main__":

	head = None
	while True:
		data = raw_input("Do you want to insert element (y/n)\n")
		if data == 'y':
			dat = raw_input("Insert your element:\n")
			if head == None:
				head = single_ll(dat)
				continue
			new_node = single_ll(dat)
			node = head
			while(node.next != None):
				node = node.next
			node.next = new_node
		else:
			single_ll.print_ll(head)	
			break
