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

    def print(self):
        if self.head == Node:
            print ("Linked list is Empty")
            return
        itr = self.head
        while(itr):
            print(str(itr.data) + " ",end='')
            itr = itr.next

    def IntersectionOptimal(self  , l1, l2):
        p1 = l1
        p2 = l2
        l1switch = False
        l2switch = False

        while (p1 or not l1switch) and (p2 or not l2switch):
            if (p1 == p2):
                return True
            p1 = p1.next
            p2 = p2.next

            if p1 is None and not l1switch:
                p1 = l2
                l1switch = True
            if p2 is None and not l2switch:
                p2 = l1
                l2switch = True
        return  False
if __name__ == '__main__':
    obj = linkedList()
    obj1 = linkedList()

    obj.insertAtEnd(1)
    obj.insertAtEnd(2)
    obj.insertAtEnd(3)
    obj.insertAtEnd(4)
    head = obj.insertAtEnd(5)
    obj.print()
    print()

    obj1.insertAtEnd(21)
    obj1.insertAtEnd(32)
    obj1.insertAtEnd(42)
    obj1.insertAtEnd(52)
    # obj1.head.next.next.next = obj.head.next.next
    head1 = obj1.insertAtEnd(62)
    obj1.print()
    print()

    print(obj.IntersectionOptimal(head , head1))

