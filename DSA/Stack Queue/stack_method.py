class stack:
    def __init__(self):
        self.stack = []
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        if self.isEmpty():
            return 'stack is empty.'
        return self.stack.pop()
    def peek(self):
        if self.isEmpty():
            return 'stack is empty.'
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)
    
mystack = stack()
mystack.push('A')
mystack.push('B')
mystack.push('C')
print('stack: ',mystack.stack)      # stack:  ['A', 'B', 'C']
print('pop: ',mystack.pop())        # pop:  C
print('peek: ',mystack.peek())      # peek:  B
print('isEmpty: ',mystack.isEmpty())    # isEmpty:  False
print('size: ',mystack.size())      # size:  2

# output :
'''
    stack:  ['A', 'B', 'C']
    pop:  C
    peek:  B
    isEmpty:  False
    size:  2
'''