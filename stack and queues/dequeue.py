# from collections import deque

# data = deque()
# data.append('Caleb')
# element = data.popleft()

# print(element, data)

# using a class
class Stack:
    def __init__(self):
        self._data = []
    
    def push(self, data):
        self._data.append(data)
    
    def pop(self):
        return self._data.pop()
    
    def peek(self): # Return the next number to be popped.
        return self._data[len(self._data) - 1]

stack = Stack()
stack.push(10)
print(stack.peek())
test = stack.pop()
print(test)