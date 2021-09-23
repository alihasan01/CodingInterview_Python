class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
# Time Complexity O(n)
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

    def print(self , head):
        if head == Node:
            print ("Linked list is Empty")
            return
        itr = head
        while(itr):
            print(str(itr.data) + " ",end='')
            itr = itr.next
    def kthTolast(self , k):
        slow = self.head
        fast = self.head

        for _ in range (k):
            if fast:
                fast = fast.next
            else:
                return None

        while fast:
            fast = fast.next
            slow = slow.next

        return slow
if __name__ == '__main__':
    obj = linkedList()
    obj.insertAtEnd(1)
    obj.insertAtEnd(2)
    obj.insertAtEnd(3)
    head = obj.insertAtEnd(4)
    obj.print(head)
    print()

    head = obj.kthTolast(2)

    obj.print(head)