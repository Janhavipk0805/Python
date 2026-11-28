class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    def push(self,new_node):
        new_node.next = self.top
        self.top = new_node
    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            temp = self.top
            print("Popped element:",temp.data)
            self.top = self.top.next
    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next
    def reverse_string(self,string):
        s1 = Stack()

        for ch in string:
            s1.push(Node(ch))
            result = ""

        while s1.top:
              result = result + s1.top.data
              s1.top = s1.top.next
        print("Reversed string:",result)
    def reverse_stack(self):
        s1 = Stack()

        temp = self.top
        while temp:
            s1.push(Node(temp.data))
            temp = temp.next
            self.top = s1.top
s= Stack()
print("\nOriginal Stack:")
s.push(Node(10))
s.push(Node(20))
s.push(Node(30))
s.push(Node(40))
s.push(Node(50))
s.display()
print("\n")
s.pop()
s.pop()
print("\n")
s.reverse_string("Janhavi")
print("\nReverse stack")
s.reverse_stack()
s.display()