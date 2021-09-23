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

    def print(self, head):
        if head == None:
            print ("Linked list is Empty")
            return
        itr = head
        while(itr):
            print(str(itr.data) + " ",end='')
            itr = itr.next

    def Palindrome(self):
        # newlist = self.head
        # prev = None
        # while newlist:
        #     temp = newlist.next
        #     newlist.next = prev
        #     prev = newlist
        #     newlist = temp
    # Above code just for reversing linkedList practise

        listNew = self.head
        stack = []
        while listNew:
            stack.append(listNew.data)
            listNew = listNew.next

        current = self.head
        while current:
            i = stack.pop()
            if i == current.data:
                flag = True
            else:
                flag = False
                break
            current = current.next
        return flag

    def compareLists(self , l1 , l2):
        p1 = l1
        p2 = l2
        while (p1 and p2):
            if p1.data == p2.data:
                p1 = p1.next
                p2 = p2.next
            else:
                return False
        return True

if __name__ == '__main__':
    obj = linkedList()
    obj1 = linkedList()

    obj.insertAtEnd(1)
    obj.insertAtEnd(2)
    obj.insertAtEnd(3)
    obj.insertAtEnd(4)
    head = obj.insertAtEnd(1)
    obj.print(head)
    print()

    flag  = obj.Palindrome()

    if flag:
        print("Linked list is palindrome")
    else:
        print("Linked list is not palindrome")

