from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, num):
        self.stack.append(num)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack.pop()

    def top(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.top())  # 30
stack.pop()
print(stack.top())  # 20
print(stack.is_empty())  # False
print(stack.size())  # 2
