class Node:
    def __init__(self,book):
        self.book=book
        self.left=None
        self.right=None

    def insert(self,book):
        if book.title < self.book.title:
            if self.left is None:
                self.left=Node(book)
            else:
                self.left.insert(book)
        elif book.title > self.book.title:
            if self.right is None:
                self.right=Node(book)
            else:
                self.right.insert(book)

    def search(self,title):
        if title==self.book.title:
            return self.book
        if title<self.book.title and self.left:
            return self.left.search(title)
        if title>self.book.title and self.right:
            return self.right.search(title)

        return None

    def inorder(self,books):
        if self.left:
            self.left.inorder(books)
        books.append(self.book)
        if self.right:
            self.right.inorder(books)