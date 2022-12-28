class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None

    def push(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        self.head = Node(data,self.head)
    
    def pop(self):
        if self.head is None:
            print("Stack is empty")
            return
        self.head = self.head.next

    def print(self):
        if self.head is None:
            print("Stack is empty")
            return
        itr = self.head
        print("[",end="")
        while itr:
            print(itr.data,end=",")
            itr = itr.next
        print("]")

    def size(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
    
    def peek(self):
        return self.head.data
    
s = Stack()
s.push(2)
s.push(1)
s.print()
print("size of the stack = ",s.size())
print("Top element of the stack is ",s.peek())
s.pop()
s.print()
s.pop()
s.print()