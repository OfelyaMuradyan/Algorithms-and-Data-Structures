class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[0]
    
    def is_empty(self):
        return self.queue == None
    
    def size(self):
        return len(self.queue)
    
ob = Queue()
ob.enqueue(20)
ob.enqueue(47)
print(ob.peek())
ob.dequeue()
ob.enqueue(56)
print(ob.peek())
ob.enqueue(79)
print(ob.size())