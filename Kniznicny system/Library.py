from BST import BST
from Book import Book
class Library:
    def __init__(self):
        self.tree=BST()

    def addBook(self,title,author):
        book=Book(title,author)
        self.tree.insert(book)

    def findBook(self,title):
        return self.tree.search(title)

    def borrowBook(self,title):
        book=self.findBook(title)
        if book and not book.borrowed:
            book.borrowed=True
            return True
        return False

    def returnBook(self,title):
        book=self.findBook(title)
        if book and book.borrowed:
            book.borrowed=False
            return True
        return False

    def getBooks(self):
        return self.tree.getAllBooks()

    def saveToFile(self):
        file=open("books.txt","w",encoding="utf-8")
        for book in self.getBooks():
            file.write(book.title+";"+book.author+";"+str(book.borrowed)+"\n")
        file.close()

    def loadFromFile(self):
        try:
            file=open("books.txt", "r",encoding="utf-8")
            for line in file:
                data=line.strip().split(";")
                book=Book(data[0],data[1])
                book.borrowed=(data[2]=="True")
                self.tree.insert(book)

            file.close()

        except FileNotFoundError:
            pass