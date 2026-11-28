class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # PUSH
    def push(self, newnode):
        newnode.next = self.top
        self.top = newnode

    # POP
    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            temp = self.top
            print("Popped element:", temp.value)
            self.top = self.top.next

    # DISPLAY
    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            temp = self.top
            print("Stack contains:")
            while temp:
                print(temp.value)
                temp = temp.next

    # REVERSE STRING
    def reverse_string(self, string):
        s1 = Stack()

        for ch in string:
            s1.push(Node(ch))

        result = ""

        while s1.top:
            result = result + s1.top.value
            s1.top = s1.top.next

        print("Reversed string:", result)

    # REVERSE STACK USING ANOTHER STACK
    def reverse_stack(self):
        s1 = Stack()

        temp = self.top

        while temp:
            s1.push(Node(temp.value))
            temp = temp.next

        self.top = s1.top


# MAIN PROGRAM

s = Stack()

# PUSH
s.push(Node(10))
s.push(Node(20))
s.push(Node(30))
s.push(Node(40))

# DISPLAY
print("Original Stack:")
s.display()

# POP
print("\nPop Operation:")
s.pop()
s.display()

# REVERSE STACK
print("\nReverse Stack:")
s.reverse_stack()
s.display()

# REVERSE STRING
print("\nReverse String:")
s.reverse_string("PYTHON")