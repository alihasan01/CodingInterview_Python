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

    def print(self,head):
        if head == None:
            print ("Linked list is Empty")
            return
        itr = head
        while(itr):
            print(str(itr.data) + " ",end='')
            itr = itr.next

    def partition(self , head , key):
        # less = Node(None)
        # equalGreater = Node(None)
        # LessG = less
        # GreaterG = equalGreater
        # while head:
        #     if head.data < key:
        #         LessG.next = head
        #         LessG = LessG.next
        #     else:
        #         GreaterG.next = head
        #         GreaterG = GreaterG.next
        #     head = head.next
        # LessG.next = equalGreater.next
        # return less.next

        lessThan = Node(None)
        greaterEqual = Node(None)
        headL = lessThan
        headG = greaterEqual
        while head:
            if head.data < key:
                headL.next = head
                headL = headL.next
            else:
                headG.next = head
                headG = headG.next
            head = head.next
        headL.next = greaterEqual.next
        headG.next = None
        return lessThan.next

if __name__ == '__main__':
    obj = linkedList()
    obj.insertAtEnd(1)
    obj.insertAtEnd(4)
    obj.insertAtEnd(3)
    obj.insertAtEnd(2)
    obj.insertAtEnd(5)
    head = obj.insertAtEnd(2)
    obj.print(head)
    print()

    head1 = obj.partition(head ,5 )
    # obj.deleteNode(head)

    obj.print(head1)