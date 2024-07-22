class Minstack:
    def __init__(self):
        self.items = []
        self.min_stack = []
    
    def is_empty(self):
        return not self.items

    def push(self, val):
        self.items.append(val)
        if not self.min_stack or val<=self.min_stack[-1]:
            self.min_stack.append(val)
        return f'{val} is pushed into stack'
    
    def pop(self):
        popped = self.items.pop()
        if popped == self.min_stack[-1]:
            self.min_stack.pop()
            return popped

    def get_min(self):
        if self.is_empty():
            return None
        return self.min_stack[-1]
    
    def top(self):
        if self.is_empty():
            return None
        return self.items[-1]
    

stack = Minstack()
print('Stack is Empty :',stack.is_empty())
print(stack.push(5))
print('Minimum : ',stack.get_min())
print('Top : ',stack.top())
print(stack.push(10))
print(stack.push(3))
print('Minimum : ',stack.get_min())
print('Top : ',stack.top())
print(stack.push(1))
print('Minimum : ',stack.get_min())
print('Top : ',stack.top())
print('Popped element',stack.pop())
print('Stack is Empty :',stack.is_empty())
