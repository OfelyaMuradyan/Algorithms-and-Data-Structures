from stack import Stack
from Queue import Queue

class TreeNode:
    def __init__(self, data = 0):
        self.data = data
        self.left = None
        self.right  = None

class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None
    
    def get_root_data(self):
        if not self.is_empty():
            return self.root.data
        
    def clear(self):
        if self.is_empty():
            return
        st = Stack()
        st.push(self.root)
        
        while not st.is_empty():
            current = st.top()
            st.pop()
            if current.left is not None:
                st.push(current.left)
            if current.right is not None:
                st.push(current.right)
            current.left = current.right = None
        self.root = None

    def _clear(self, node):
        if node is None:
            return
        self._clear(node.left)
        self._clear(node.right)
        node.left = None
        node.right = None

    def clear_r(self):
        if self.is_empty():
            return
        self._clear(self.root)



    def set_root_data(self, new_data):
        if not self.is_empty():
            self.root.data = new_data

###### add

    def add(self, data):
        node = TreeNode(data)
        if self.root == None:
            self.root = node
        else:
            current = self.root
            while(current != None):
                if data > current.data:
                    if current.right is None:
                        current.right = node
                        return
                    else:
                        current = current.right
                elif data < current.data:
                    if current.left is None:
                        current.left = node
                        return
                    else:
                        return
                else:
                    return 

    def add_rec(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._add_recursive(self.root, data)

    def _add_recursive(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = TreeNode(data)
            else:
                self._add_recursive(current.left, data)
        elif data > current.data:
            if current.right is None:
                current.right = TreeNode(data)
            else:
                self._add_recursive(current.right, data)

####### inorder traversal

    def _inorder_recursive(self, node):
        if node != None:
            self._inorder_recursive(node.left)
            print(node.data)
            self._inorder_recursive(node.right)
    
    def inorder_rec(self):
        if self.root == None:
            return
        else:
            self._inorder_recursive(self.root)

    def inorder(self):
        if self.root is None:
            return
        self.stack = Stack()
        current = self.root
        while(current != None or not self.stack.is_empty()):
            while(current != None):
                self.stack.push(current)
                current = current.left
            current = self.stack.top()
            print(current.data)
            self.stack.pop()
            current = current.right

######  preorder traversal

    def preorder(self):
        if self.root == None:
            return
        st = Stack()
        st.push(self.root)
        while not st.is_empty():
            node = st.top()
            print(node.data)
            st.pop()
            if node.right != None:
                st.push(node.right)
            if node.left != None:
                st.push(node.left)

    def _preorder(self, node):
        if node == None:
            return
        print(node.data)
        self._preorder(node.left)
        self._preorder(node.right)

    def preorder_rec(self):
        if self.root == None:
            return
        else:
            self._preorder(self.root)

#######   postorder traversal

    def postorder(self):
        if self.root == None:
            return
        st = Stack()
        st.push(self.root)
        out = Stack()
        while not st.is_empty():
            node = st.top()
            st.pop()
            out.push(node.data)
            if node.left != None:
                st.push(node.left)
            if node.right != None:
                st.push(node.right)
        while not out.is_empty():
            print(out.top())
            out.pop()
        
    def _postorder(self, node):
        if node == None:
            return
        self._postorder(node.left)
        self._postorder(node.right)
        print(node.data)

    def postorder_rec(self):
        if self.root == None:
            return
        else:
            self._postorder(self.root)

#######  level order traversal

    def level_order(self):
        if self.root == None:
            return
        q = Queue()
        q.enqueue(self.root)
        while not q.is_empty():
            node = q.peek()
            q.dequeue()
            print(node.data)
            if node.left != None:
                q.enqueue(node.left)
            if node.right != None:
                q.enqueue(node.right)

######  get height

    def get_height(self):
        height = 0
        if self.root == None:
            return height
        q = Queue()
        q.enqueue(self.root)
        while not q.is_empty():
            level = q.size()
            height += 1
            for i in range(level):
                node = q.peek()
                q.dequeue()
                if node.left != None:
                    q.enqueue(node.left)
                if node.right != None:
                    q.enqueue(node.right)
        return height 
    
    def _get_height(self, node):
        if node == None:
            return 0
        leftHeight = self._get_height(node.left)
        #print(leftHeight)
        rightHeight = self._get_height(node.right)
        #print(rightHeight,"r")
        return 1 + max(leftHeight, rightHeight)
    
    def get_height_r(self):
        if self.root == None:
            return 0
        return self._get_height(self.root) 
    
####### remove

    def _remove(self, node, key):
        # finding key
        if node == None:
            return node
        elif node.data > key:
            node.left = self._remove(node.left, key)
        elif node.data < key:
            node.right = self._remove(node.right, key)
        else:
            # if node is found
            if node.left == None:
                return node.right
            elif node.right == None:
                return node.left
            else:
                successor = self.findMin(node.right)
                node.data = successor.data
                self._remove(node.right, successor.data)
            return node
    
    def remove_r(self, key):
        if self.root == None:
            return 
        return self._remove(self.root, key)

    def findMin(self, node):
        current = node
        while current and current.left:
            current = current.left
        return current

######  contains

    def contains(self, data):
        current = self.root
        while current:
            if data > current.data:
                current = current.right
            elif data < current.data:
                current = current.left
            else:
                return True
        return False
    
    def _contains(self, node, data):
        if node is None:
            return False
        if node.data == data:
            return True
        elif node.data > data:
            return self._contains(node.left, data)
        elif node.data < data:
            return self._contains(node.right, data)
        
    def contains_r(self, data):
        if not self.is_empty():
            return self._contains(self.root, data)

###### number of nodes

    def _get_number_of_nodes(self, node):
        if node is None:
            return 0
        return 1 + self._get_number_of_nodes(node.left) + self._get_number_of_nodes(node.right)

    def get_number_of_nodes_r(self):
        if self.is_empty():
            return 0
        return self._get_number_of_nodes(self.root)
    
    def get_number_of_nodes(self):
        if self.root is None:
            return 0
        
        num = 0
        st = Stack()
        st.push(self.root)

        while not st.is_empty():
            num += 1
            current = st.top()
            st.pop()

            if current.left is not None:
                st.push(current.left)
            if current.right is not None:
                st.push(current.right)
        return num
    





ob = BST()
# print(ob.is_empty())
ob.add(25)
# print(ob.is_empty())
ob.add(14)
ob.add(28)
ob.add(27)
# ob.add(30)
# ob.add(29)
# ob.add(35)
#print(ob.set_root_data(2))


ob1 = BST()
ob1.add_rec(57)
ob1.add_rec(24)
ob1.add_rec(86)
ob1.add_rec(31)
ob1.add_rec(5)
ob1.add_rec(79)

# print(ob.get_number_of_nodes())

ob1.inorder()
# ob.inorder_rec()
ob1.clear_r()
# ob.preorder()
ob1.preorder_rec()

# ob.postorder()
# ob1.postorder_rec()

# ob.level_order()

# print(ob.get_height())
# print(ob1.get_height_r())

# ob.remove_r(28)
# ob.inorder()

# print(ob.contains(26))
# print(ob1.contains_r(57))