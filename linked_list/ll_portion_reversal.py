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
			#print(node.data)
			node = node.next
		ll_str = ll_str + str(node.data)
		print(ll_str)

	@staticmethod
	def print_ll_using_rec(node):
		if node != None:
			print(node.data)
			single_ll.print_ll_using_rec(node.next)

	@staticmethod
	def do_portion_reversal(node, portion):
		current = node 
		next  = None
		prev = None
		count = 0
		while(current != None and count < portion):
			next = current.next
			current.next = prev
			prev = current
			current = next
			count += 1

		if next is not None:
			node.next = single_ll.do_portion_reversal(next, portion)
		return prev

	@staticmethod
	def do_portion_rev(node, portion):
		count = 0
		stack = []
		while(count < portion):
			try:
				stack.append(node)
				node = node.next
			except:
				break
			count += 1

		temp = stack[portion - 1].next
		count = portion - 1
		while(count > 0):
			try:
				stack[count].next = stack[count - 1]
			except:
				pass
			count -= 1

		stack[0].next = temp

		if temp.next != None:
			stack[0].next = single_ll.do_portion_rev(temp, portion)
	
		return stack[portion - 1]	
		#if 
		#do_portion_rev(stack[0].next, portion)
				

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
			portion = int(raw_input("Enter value of portion for reversal\n"))
			head = single_ll.do_portion_rev(head, portion)
			#head = single_ll.do_portion_reversal(head, portion)
			print("LL after portion reversal\n", head.data)
			single_ll.print_ll(head)	
			break
