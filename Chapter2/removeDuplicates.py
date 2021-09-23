class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Time Complexity O(n)
# Space complexity Complexity O(n)

class linkedList:
    def __init__(self):
        self.head = None

    def insertAtStart(self,data):
        node = Node(data , self.head)
        self.head = node
    def insertAtEnd(self,data):
        if self.head is None:
            self.head = Node(data , None)
            return
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data, None)
        return self.head

    def print(self):
        if self.head == Node:
            print ("Linked list is Empty")
            return
        itr = self.head
        while(itr):
            print(str(itr.data) + " ",end='')
            itr = itr.next
    def removeDuplicates(self ):

        mySet = set()
        if self.head is None:
            print("linked List is empty")
            return
        itr = self.head
        mySet.add(self.head.data)
        while itr and itr.next:
            if itr.next.data in mySet:
                itr.next = itr.next.next
            else:
                mySet.add(itr.next.data)
                itr = itr.next
        return self.head
if __name__ == '__main__':
    obj = linkedList()
    obj.insertAtEnd(3)
    obj.insertAtEnd(3)
    obj.insertAtEnd(31)
    obj.insertAtEnd(3)
    obj.print()
    print()

    head = obj.removeDuplicates()

    obj.print()