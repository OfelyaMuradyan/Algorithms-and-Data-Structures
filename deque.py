class Deque:
    def __init__(self):
        self.deque = []

    def push_front(self, element):
        self.deque.insert(0,element)

    def push_back(self, element):
        self.deque.append(element)

    def pop_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.deque.pop(0)

    def pop_back(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.deque.pop()

    def front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.deque[0]
    
    def back(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.deque[self.size() - 1]

    def is_empty(self):
        return len(self.deque) == 0
    
    def size(self):
        return len(self.deque)
    
    def clear(self):
        self.deque.clear()
    
    def operator(self, index):
        return self.deque[index]
    
    def insert(self, position, element):
        self.deque.insert(position,element)

    def erase(self, position):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.deque.pop(position)
    
ob = Deque()
ob.push_front(5)
ob.push_front(15)
ob.push_back(19)
ob.erase(2)
print(ob.back())

