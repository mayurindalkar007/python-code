class bst:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    @staticmethod
    def print_bst_inorder(node):

        if node.left != None:
            bst.print_bst_inorder(node.left)

        print(node.data)

        if node.right != None:
            bst.print_bst_inorder(node.right)

    @staticmethod
    def print_bst_preorder(node):
        print(node.data)
        if node.left != None:
            bst.print_bst_preorder(node.left)
        if node.right != None:
            bst.print_bst_preorder(node.right)

    @staticmethod
    def print_bst_postorder(node):
        if node.left != None:
            bst.print_bst_postorder(node.left)
        if node.right != None:
            bst.print_bst_postorder(node.right)
        print(node.data)

    @staticmethod
    def find_successor(node):
        par = None
        if node.right:
            tmp = node.right
            par = node
            while(tmp.left):
                par = tmp
                tmp = tmp.left
        return tmp,par
            

    @staticmethod
    def delete_node(node, data, parent):
        if node.data == data:
            if not node.left and not node.right:
                print('in leaf')
                print(node.data)
                if parent.left.data == node.data:
                    parent.left = None
                else:   
                    parent.right = None
                return
            if node.left and not node.right:
                node.data = node.left.data
                bst.delete_node(node.left, node.left.data, node)
            if node.right and not node.left:
                node.data = node.right.data
                bst.delete_node(node.right, node.right.data, node)
            if node.right and node.left:
                print('successor node is')
                successor_node, p = bst.find_successor(node)
                print(successor_node.data)
                node.data = successor_node.data
                bst.delete_node(successor_node, successor_node.data, p)

        if node.right and data > node.data:
            bst.delete_node(node.right, data, node)
        if node.left and data < node.data:
            bst.delete_node(node.left, data, node)
        if not node.left and not node.right:
            print('Data not found')
            return
                
        #while True:
        #   if dat <= node.data and node.left != None:
        #       node = node.left
        #   if dat > node.data and node.right != None:
        #       node = node.right
        #   if dat <= node.data and node.left == None:
        #       node.left = new_node
        #   if dat > node.data and node.right == None:
        #       node.right = new_node


    @staticmethod
    def find_height(node):
        if node == None:
            return 0
        return max(bst.find_height(node.left), bst.find_height(node.right)) + 1


if __name__ == "__main__":
    root = None
    while True:
        choice = raw_input("Enter choice:\n1. Insert\n2. Display\n3. Delete\n4. Find Height\n")
        if choice == '1':
            dat = raw_input("Insert Element:\n")
            if root == None:
                root = bst(dat)
                continue
            new_node = bst(dat)
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
            print("Inorder traversal")
            bst.print_bst_inorder(root)
            print("Preorder traversal")
            bst.print_bst_preorder(root)
            print("Preorder traversal")
            bst.print_bst_postorder(root)
        elif choice == '3':
            dat = raw_input("Enter Element to delete:\n")
            bst.delete_node(root, dat, None)
        elif choice == '4':
            print('Height is:\n')
            print(bst.find_height(root))        
