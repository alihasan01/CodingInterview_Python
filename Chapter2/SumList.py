class Node:
    def __init__(self, data , next=None):
        self.data = data
        self.next = next

# Time Complexity O(n)
# Space complexity Complexity O(n)
class linkedList:
    def __init__(self):
        self.head = None

    def insertAtStart(self, data):
        node = Node(data, self.head)
        self.head = node

    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data, None)
        return self.head

    def print(self, head):
        if head == None:
            print("Linked list is Empty")
            return
        itr = head
        while (itr):
            print(str(itr.data) + " ", end='')
            itr = itr.next

    def sumList(self, l1, l2):
        sumList = Node(None)
        cur = sumList
        carryOver = False
        while l1 or l2 or carryOver:
            newNode = Node(0)

            if l1:
                newNode.data += l1.data
                l1 = l1.next

            if l2:
                newNode.data += l2.data
                l2 = l2.next

            if carryOver:
                newNode.data += 1
                carryOver = False

            if newNode.data > 9:
                carryOver = True
                newNode.data -= 10

            cur.next = newNode
            cur = cur.next

        return sumList.next

if __name__ == '__main__':
    obj = linkedList()
    obj1 = linkedList()

    obj.insertAtEnd(9)
    obj.insertAtEnd(1)
    head = obj.insertAtEnd(6)
    obj.print(head)
    print()

    obj1.insertAtEnd(4)
    obj1.insertAtEnd(3)
    # obj1.head.next.next.next = obj.head.next.next
    head1 = obj1.insertAtEnd(2)
    obj1.print(head1)
    print()

    result  = obj.sumList(head , head1)
    obj1.print(result)