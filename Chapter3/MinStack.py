class MinStack:
    def __init__(self):
        self.items = []

    def push (self , item):
        if len(self.items) == 0:
            self.items.append((item, item))
        else:
            self.items.append((item, min(item , self.items[-1][1])))

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()[0]

    def min(self):
        if len(self.items) > 0:
            return self.items[-1][1]

if __name__ == '__main__':
    a = MinStack()
    a.push(10)
    a.push(4)
    a.push(6)

    print(a.min())
    # print(a.pop())
    print(a.min())
    # print(a.pop())