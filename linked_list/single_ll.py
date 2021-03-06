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
    def rev_ll(node):
        if node.next != None:
            next_node = single_ll.rev_ll(node.next)
            next_node.next = node
            
         
        return next_node
        
        

if __name__ == "__main__":

    head = None
    while True:
        data = raw_input("Enter Choice:\n1. Enter LL:\n2. Print LL\n3. Reverse LL\n4. Exit\n")
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
            head = single_ll.rev_ll(head)
        elif data == '4':
            print('Bye!')
            break
        else:
            print('Wrong Entry')
