from stack import Stack

class TreeNode:
    def __init__(self, value, left = None, right = None, height = 1):
        self.left = left
        self.right = right
        self.value = value
        self.height = height

class AVL:
    def __init__(self):
        self.root = None

    def getHeight(self, node):
        if node is None:
            return 0
        return node.height

    def getBalance(self, node):
        if node != None:
            return self.getHeight(node.left) - self.getHeight(node.right)
        return 0
        
    def rightRotation(self, node):
        x = node.left
        tmp = x.right
        # rotation
        x.right = node
        node.left = tmp
        node.height = max(self.getHeight(node.left),self.getHeight(node.right)) + 1
        x.height = max(self.getHeight(x.left), self.getHeight(x.right)) + 1
        return x 
        
    
    def leftRotation(self, node):
        y = node.right
        tmp = y.left
        # rotation
        y.left = node
        node.right = tmp
        node.height = max(self.getHeight(node.left),self.getHeight(node.right)) + 1
        y.height = max(self.getHeight(y.left), self.getHeight(y.right)) + 1
        return y 
    
    def insert(self, node, data):
        if node == None:
            return TreeNode(data) 
        if data > node.value:
            node.right = self.insert(node.right, data)
        elif data < node.value:
            node.left = self.insert(node.left, data)
        else:
            return node
        
        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) + 1

        balance = self.getBalance(node)
        if balance > 1 and data < node.left.value:
            return self.rightRotation(node)
        if balance < -1 and data > node.right.value:
            return self.leftRotation(node)
        if balance > 1 and data > node.left.value:
            node.left = self.leftRotation(node.left)
            return self.rightRotation(node)
        if balance < -1 and data < node.right.value:
            node.right = self.rightRotation(node.right)
            return self.leftRotation(node)
        return node
    
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
            print(current.value)
            self.stack.pop()
            current = current.right

    def search(self, data):
        current = self.root
        while current:
            if data > current.value:
                current = current.right
            elif data < current.value:
                current = current.left
            else:
                return current
        return 
    
    def _delete(self, node, key):
        # finding key
        if node == None:
            return node
        elif node.value > key:
            node.left = self._delete(node.left, key)
        elif node.value < key:
            node.right = self._delete(node.right, key)
        else:
            # if node is found
            if node.left == None:
                return node.right
            elif node.right == None:
                return node.left
            else:
                successor = self.findMin(node.right)
                node.data = successor.data
                self._delete(node.right, successor.data)
        
        balance = self.getBalance(node)
        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) + 1

        if balance > 1:
            if self.getBalance(node.left) >= 0:  # Left-Left Case
                return self.rightRotation(node)
            else:  # Left-Right 
                node.left = self.leftRotation(node.left)
                return self.rightRotation(node)

        if balance < -1:
            if self.getBalance(node.right) <= 0:  # Right-Right 
                return self.leftRotation(node)
            else:  # Right-Left 
                node.right = self.rightRotation(node.right)
                return self.leftRotation(node)

        return node
    
    def delete_r(self, key):
        if self.root == None:
            return 
        return self._delete(self.root, key)

    def findMin(self, node):
        current = node
        while current and current.left:
            current = current.left
        return current
    
ob = AVL()
ob.root = ob.insert(ob.root, 10)
ob.root = ob.insert(ob.root, 20)
ob.root = ob.insert(ob.root, 30)
ob.root = ob.insert(ob.root, 40)
ob.root = ob.insert(ob.root, 50)
ob.root = ob.insert(ob.root, 25)
ob.delete_r(40)
ob.inorder()
