class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
    def display(self):
       print("Book title:",self.title)
       print("Book author:",self.author)
       print("Book price:",self.price)
b1 = Book("Python programming","James",550)
b1.display()