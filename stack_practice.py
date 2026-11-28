class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
       self.top = None

    #Push operation
    def push(self,new_node):
        new_node.next = self.top
        self.top = new_node

    #Pop operation
    def pop(self):
       if self.top is None:
           print("Stack is empty")
       else:
          temp = self.top
          print("Popped element:",temp.value)
          self.top = self.top.next

    # Display elements
    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            temp = self.top
            print("Stack contains:")
            while True:
             print(temp.value)
             temp = temp.next
    # Reverse string
    def reverse_string(self,string):
        s1 = Stack()

        for ch in string:
            s1.push(Node(ch))

        result =""

        while s1.top:
            result = result + s1.top.value
            s1.top = s1.top.next
        print("Reversed string:",result)

     # Reverse stack on another stack
    def reverse_stack(self):
        s1 = Stack()
        temp = self.top
        while temp:
           s1.push(Node(temp.value))
           temp = temp.next
        self.top = s1.top

# Main program
s = Stack()

#Push elements
s.push(Node(10))
s.push(Node(20))
s.push(Node(30))
s.push(Node(40))
s.push(Node(50))
s.push(Node(60))
s.push(Node(70))
s.push(Node(80))
s.push(Node(90))
s.push(Node(100))

#Display elements
print("\nOriginal elements:")


# Pop elements
s.pop()

#Reverse stack
print("Reverse stack elements:")
s.reverse_stack()
s.display()

#Reverse string
print("Reverse String:")
s.reverse_string("Python")
s.display()
