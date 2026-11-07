class MinStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.min_e = 10**10
    
    def push(self, value):
        self.value = value
        self.stack1.append(self.value)
        if self.value <= self.min_e:
            self.min_e = self.value
            self.stack2.append(self.value)

    def pop(self):
        pop_e = self.stack1.pop()
        if pop_e == self.stack2[-1]:
            self.stack2.pop()
        return pop_e

    def top(self):
        print(self.stack1[-1])

    def get_min(self):
        print(self.stack2[-1])


stack = MinStack()
stack.push(-2)
stack.push(0)
stack.push(-3)
stack.get_min()
stack.pop()
stack.top()
stack.get_min()