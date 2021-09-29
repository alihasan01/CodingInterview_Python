class SetOfStack:
    def __init__(self, capacity = 10):
        if (capacity < 1):
            raise ValueError("Capacity atleast 1")
        self.capacity = capacity
        self.stacks = [[]]

    def push(self , item):
        if (len (self.stacks[-1]) == self.capacity):
            self.stacks.append([])
        self.stacks[-1].append(item)

    def pop(self):
        if len(self.stacks[-1]) == 0:
            if len(self.stacks) == 1:
                raise ValueError("pop from empty stack")
            else:
                self.stacks.pop()
        return self.stacks[-1].pop()

if __name__ == '__main__':
    a = SetOfStack()
    a.push(10)
    a.push(4)
    a.push(6)
    a.push(10)
    a.push(4)
    a.push(6)
    a.push(10)
    a.push(4)
    a.push(6)
    a.push(10)
    a.push(4)
    a.push(6)

    print(a.pop())
    a.pop()
    a.pop()
    a.pop()
