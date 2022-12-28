class Node:
    def __init__(self,data = None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head is None:
            return True
        return False

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count

    def append(self,data):
        if self.isempty():
            self.head = Node(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)

    def insert_at_beginning(self,data):
        if self.isempty():
            self.head = Node(data)
            return
        temp_node = Node(data,self.head)
        self.head = temp_node

    def print(self):
        if self.isempty():
            print("Linked List is empty")
            return
        itr = self.head
        print("[",end="")
        while itr:
            print(itr.data,end=",")
            itr = itr.next
        print("]") 

    def insert_values(self,data):
        for datum in data:
            self.append(datum)

    def insert_at(self,data,pos):
        if pos<0 or pos>=self.get_length():
            print("Invalid position")
            return
        if pos == 0:
            self.insert_at_beginning(data)
            return
        itr = self.head
        for _ in range(pos-1):
            itr = itr.next
        temp_node = itr.next
        itr.next = Node(data,temp_node)

    def remove_at(self,pos):
        if pos<0 or pos>self.get_length():
            print("Invalid position")
            return
        if pos == 0:
            self.head = self.head.next
            return
        itr = self.head
        for _ in range(pos-1):
            itr = itr.next
        itr.next = itr.next.next
if __name__ == "main":
    list = LinkedList()
    list.insert_values([1,2,3,4,5])
    list.print()
    list.insert_at(7,2)
    list.print()
    list.remove_at(2)
    list.print()
        
