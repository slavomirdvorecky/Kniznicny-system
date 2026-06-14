from Node import Node
class BST:
    def __init__(self):
        self.root=None

    def insert(self,book):
        if self.root is None:
            self.root=Node(book)
        else:
            self.root.insert(book)

    def search(self,title):
        if self.root:
            return self.root.search(title)
        return None

    def getAllBooks(self):
        books=[]
        if self.root:
            self.root.inorder(books)
        return books