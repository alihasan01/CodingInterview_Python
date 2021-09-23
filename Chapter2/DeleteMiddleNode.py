class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
# Time Complexity O(1)
# Space complexity Complexity O(1)
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
        if head == Node:
            print ("Linked list is Empty")
            return
        itr = head
        while(itr):
            print(str(itr.data) + " ",end='')
            itr = itr.next

    def deleteNode(self, node):
        node.data = node.next.data
        node.next = node.next.next

    def DeleteMiddle(self ):
        slow = self.head
        fast = self.head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return self.head
if __name__ == '__main__':
    obj = linkedList()
    obj.insertAtEnd(1)
    obj.insertAtEnd(2)
    obj.insertAtEnd(3)
    obj.insertAtEnd(4)
    head = obj.insertAtEnd(5)
    obj.print()
    print()

    head = obj.DeleteMiddle()
    # obj.deleteNode(head)

    obj.print()