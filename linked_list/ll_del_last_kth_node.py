class ll_del_last_kth_node:
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
            ll_del_last_kth_node.print_ll_using_rec(node.next)

    @staticmethod
    def rev_ll(node):
        if node.next != None:
            next_node = ll_del_last_kth_node.rev_ll(node.next)
            next_node.next = node
            
        return next_node

    @staticmethod
    def delete_kth_from_last(node, k, index, prev):
        if node.next != None:
            ll_del_last_kth_node.delete_kth_from_last(node.next, k, index, node) 
        index[0]+=1 
        print(node.data, index[0], k)
        if index[0] == k:
            print('in if')
            if prev != None:
                prev.next = node.next
        if prev == None:
            return node.next
        return node
        
if __name__ == "__main__":

    head = None
    while True:
        data = raw_input("Enter Choice:\n1. Enter LL:\n2. Print LL\n3. Reverse LL\n4. Delete kth from last\n5. Exit\n")
        if data == '1':
            dat_list = raw_input("Insert your LL:\n").strip().split()
            for dat in dat_list:
                if head == None:
                    head = ll_del_last_kth_node(dat)
                    continue
                new_node = ll_del_last_kth_node(dat)
                node = head
                while(node.next != None):
                    node = node.next
                node.next = new_node
        elif data == '2':
            ll_del_last_kth_node.print_ll(head)
        elif data == '3':
            head = ll_del_last_kth_node.rev_ll(head)
        elif data == '4':
            k = int(raw_input('Enter value of k:\n'))
            head = ll_del_last_kth_node.delete_kth_from_last(head, k, [0], None)
        elif data == '5':
            print('Bye!')
            break
        else:
            print('Wrong Entry')
