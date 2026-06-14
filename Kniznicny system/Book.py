class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.borrowed=False

    def __str__(self):
        stav="Požičaná" if self.borrowed else "Dostupná"
        return f"{self.title} - {self.author} ({stav})"