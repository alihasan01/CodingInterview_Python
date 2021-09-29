
class ThreeStack:
    def __init__(self , capacity = 5):
        capacity = capacity * 3

        self.items = [None] * capacity

        self.tops = [0, capacity // 3 ,2 * (capacity // 3)]

        self.limits = [capacity // 3 ,2 * (capacity // 3) , capacity ]
    def push(self , stack , item):
        if stack > 2:
            raise ValueError("stack does not exist")

        if self.tops[stack] >= self.limits[stack]:
            raise Exception(f"stack {stack} is full")

        self.items[self.tops[stack]] = item
        self.tops[stack] += 1

    def pop(self, stack):

        if stack > 2:
            raise ValueError("stack does not exist")

        top = self.tops[stack] - 1

        if top < 0 or self.items[top] == None:
            raise IndexError("pop from empty stack")


        item = self.items[top]
        self.items[top] = None
        self.tops[stack] = top

        return item

if __name__ == '__main__':
    a = ThreeStack()
    a.push(0, 4)  # stack 0, push 4
    a.push(1, 5)  # stack 1, push 4
    a.push(2, 7)  # stack 2, push 5
    a.push(0, 6)  # stack 0, push 6
    print(a.pop(0))  # 6
    print(a.pop(1))  # 5
    print(a.pop(2))  #