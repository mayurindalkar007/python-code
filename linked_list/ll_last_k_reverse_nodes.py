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
	
	@staticmethod
	def last_k_nodes_using_stack(node, k):
		stack = []
		end = int(k)+1
		while(node.next != None):
			stack.append(node.data)
			node = node.next
		stack.append(node.data)
		print(stack[-1:-end:-1])

	@staticmethod
	def last_k_nodes_using_recursion(node, count, k):
		if node.next != None:
			single_ll.last_k_nodes_using_recursion(node.next, count, k)
		count[0] += 1
		if count[0] <= k:
			print(node.data)

if __name__ == "__main__":

	head = None
	while True:
		data = raw_input("Enter Choice:\n1. Enter LL:\n2. Print LL\n3. Print last K nodes in reverse order\n4. Exit\n")
		if data == '1':
			dat_list = raw_input("Insert your LL:\n").strip().split()
			for dat in dat_list:
				if head == None:
					head = single_ll(dat)
					continue
				new_node = single_ll(dat)
				node = head
				while(node.next != None):
					node = node.next
				node.next = new_node
		elif data == '2':
			single_ll.print_ll(head)	
		elif data == '3':
			k = int(raw_input('Enter K:\n'))
			count = [0]
			single_ll.last_k_nodes_using_stack(head, k)
			single_ll.last_k_nodes_using_recursion(head, count, k)
		elif data == '4':
			print('Bye!')
			break
		else:
			print('Wrong Entry')
		
			
