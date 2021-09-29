class SortStack:
    def __init__(self):
        self.stack = []
    def push(self , item):
        self.stack.append(item)

    def SortStackFunction(self):

        tempStack = []
        while (len (self.stack) != 0):
            temp = self.stack.pop()

            while (len (tempStack) != 0 and tempStack[-1] > temp):
                self.stack.append(tempStack.pop())

            tempStack.append(temp)

        return tempStack


if __name__ == '__main__':
    a = SortStack()
    a.push(34)
    a.push(3)
    a.push(31)
    a.push(98)
    a.push(92)
    a.push(23)

    sortedStack = a.SortStackFunction()

    for i in range(len(sortedStack)-1, -1, -1):
        print(sortedStack[i], end=' ')