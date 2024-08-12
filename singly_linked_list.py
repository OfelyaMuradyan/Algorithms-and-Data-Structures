class Node:
    def __init__(self, data = 0):
        self.data = data
        self.next = None

class SinglyList:
    def __init__(self):
        self.__head  = None

    def is_empty(self):
        return self.__head == None
    
    def push_front(self, data):
        new_node = Node(data)
        
        if self.is_empty():
            self.__head = new_node
        else:
            new_node.next = self.__head
            self.__head = new_node

    def pop_front(self):
        if self.is_empty():
            raise IndexError("List is empty")
        
        tmp = self.__head
        self.__head = self.__head.next
        tmp.next = None

    def insert_after(self, prev_node, data):
        if prev_node != None:
            new_node = Node(data)
            new_node.next = prev_node.next
            prev_node.next = new_node

    def erase_after(self, prev_node):
        tmp = prev_node.next
        prev_node.next = tmp.next
        tmp.next = None

    def clear(self):
        self.__head = None

    def front(self):
        if not self.is_empty():
            return self.__head.data
        
    def reverse(self):
        current = self.__head
        prev_node = None

        while(current != None):
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node
        self.__head = prev_node

    def merge(self, other_list):
        if not self.is_empty():
            current = self.__head
            while(current.next != None):
                current = current.next
            current.next = other_list.__head

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
        ls = []
        tmp = current
        while(current != None):
            if current.data not in ls:
                ls.append(current.data)
            else:
                self.erase_after(tmp)
            tmp = current
            current = current.next

    def print_list(self):
        data = ""
        current = self.__head

        while(current != None):
            data += (str(current.data) + " -> ")
            current = current.next

        data += "None"
        return data

    def get_head(self):
        return self.__head

ob = SinglyList()
ob.push_front(24)
ob.push_front(30)
ob.push_front(15)
ob.push_front(98)
ob.push_front(30)
res = ob.print_list()
print(res)

head = ob.get_head()
second_node = head.next
# ob.insert_after(second_node,20)
# ob.erase_after(second_node)
# ob.pop_front()
# ob.clear()
# print(ob.front())

# ob1 = SinglyList()
# ob1.push_front(5)
# ob1.push_front(36)
# ob1.push_front(77)
# ob1.push_front(79)

# res = ob1.print_list()
# print(res)

# ob.reverse()
# ob.merge(ob1)
# ob.sort()
ob.unique()
res = ob.print_list()
print(res)

