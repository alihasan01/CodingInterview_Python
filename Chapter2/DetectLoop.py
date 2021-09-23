class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print(self):
        if self.head == None:
            print ("Linked list is Empty")
            return
        itr = self.head
        while(itr):
            print(str(itr.data) + " ",end='')
            itr = itr.next

    def loopBtuteForce(self, head):
        mySet = set()

        current = self.head
        while current:
            if current in mySet:
                return True
            else:
                current = current.next
                mySet.add(current)
        return False
    def loopOptimal(self ):
        slow = self.head
        fast = self.head

        while True:
            slow = slow.next
            if (fast.next != None):
                fast = fast.next.next
            else:
                return False
            if slow == fast:
                return True

        return  False
if __name__ == '__main__':
    obj = linkedList()
    # obj.insertAtEnd(1)
    # obj.insertAtEnd(2)
    # obj.insertAtEnd(6)
    # obj.insertAtEnd(2)
    # obj.insertAtEnd(6)
    # obj.print()

    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(4)
    obj.push(3)
    obj.print()
    print()

    obj.head.next.next.next = obj.head
    print(obj.loopOptimal())

