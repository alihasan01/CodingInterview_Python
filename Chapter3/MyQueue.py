# Time Complexity O(n)
# Space complexity Complexity O(n)
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def Enqueue(self, item):
        self.stack1.append(item)

    def reverseStack(self, Operator):
        if len(self.stack2) == 0:
            if len(self.stack1) == 0:
                raise ValueError("DeQueue Not Possible")
            while (len(self.stack1)):
                self.stack2.append(self.stack1.pop())

    def Dequeue(self):
        self.reverseStack("Dequeue")
        return self.stack2.pop()

    def peek(self):
        self.reverseStack("peek")
        return self.stack2[-1]

if __name__ == '__main__':
    a = MyQueue()
    a.Enqueue(10)
    a.Enqueue(4)
    a.Enqueue(6)

    print(a.Dequeue())

    a.Enqueue(3)
    print(a.Dequeue())
    print(a.Dequeue())
    print(a.Dequeue())
