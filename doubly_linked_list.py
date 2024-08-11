class Node:
    def __init__(self, data = 0):
        self.data = data
        self.next = None
        self.prev = None

class DoublyList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def is_empty(self):
        return self.__head == None
    
    def push_front(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.__head = self.__tail = new_node
        else:
             new_node.next = self.__head
             self.__head.prev = new_node
             self.__head = new_node 

    def pop_front(self):
        if self.is_empty():
            raise IndexError("List is empty")
        
        self.__head = self.__head.next
        self.__head.prev.next = None
        self.__head.prev = None

    def push_back(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.__head = self.__tail = new_node
        else:
            self.__tail.next = new_node
            new_node.prev = self.__tail
            self.__tail = new_node

    def pop_back(self):
        if self.is_empty():
            raise IndexError("List is empty")

        self.__tail = self.__tail.prev
        self.__tail.next.prev = None
        self.__tail.next = None

    def insert_after(self, prev_node, data):
        new_node = Node(data)
        if prev_node.next != None:
            new_node.next = prev_node.next
            new_node.next.prev = new_node
            prev_node.next = new_node
            new_node.prev = prev_node

    def erase_after(self, prev_node):
        if prev_node != self.__tail:
            tmp = prev_node.next
            prev_node.next = tmp.next
            prev_node.next.prev = prev_node 

    def clear(self):
        while(self.__head != None):
            self.__head = self.__head.next      

    def front(self):
        if not self.is_empty():
            return self.__head.data   

    def reverse(self):
        current = self.__head
        prev_node = None

        while current != None:
            next_node = current.next
            current.next = prev_node
            current.prev = next_node
            prev_node = current
            current = next_node
        self.__head, self.__tail = self.__tail, self.__head

    def merge_list(self, other):
        if not other.is_empty():
            self.__tail.next = other.__head
            other.__head.prev = self.__tail
            self.__tail = other.__tail

    def sort(self):
        current = self.__head

        while(current != None):
            min_node = current
            tmp = current.next

            while(tmp != None):
                if tmp.data < min_node.data:
                    min_node = tmp
                tmp = tmp.next
            min_node.data, current.data = current.data, min_node.data
            current = current.next

    def unique(self):
        current = self.__head
        di = {}
        while(current != None):
            if current.data not in di:
                di[current.data] = 1
            else:
                self.erase_after(current.prev)
            current = current.next

    def __str__(self):
        data = "None <-> "
        current = self.__head

        while(current != None):
            data += str(current.data)
            data += " <-> "
            current = current.next
        data += "None "

        # print(data)            #########  ete __str__  i anuny poxenq print, es toghn el piti grenq
        return data
    
    def get_head(self):
        return self.__head

ob = DoublyList()
ob.push_front(14)
ob.push_front(25)
ob.push_front(32)
ob.push_front(25)
ob.push_front(20)
print(ob)
# ob.print()

# head = ob.get_head()
# second_node = head.next
# ob.insert_after(second_node,20)

# ob.erase_after(second_node)
# ob.clear()

# print(ob.front())
# print(ob)

# ob.reverse()
# print(ob)

# ob1 = DoublyList()
# ob1.push_front(80)
# ob1.push_front(10)
# print(ob1)
# ob.merge_list(ob1)

ob.unique()
print(ob)