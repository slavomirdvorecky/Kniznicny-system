import tkinter
from Library import Library
window=tkinter.Tk()
window.title("Library")
library=Library()
library.loadFromFile()
titleEntry=tkinter.Entry(window)
authorEntry=tkinter.Entry(window)
listbox=tkinter.Listbox(window,width=50)

def refresh():
    listbox.delete(0, tkinter.END)
    for book in library.getBooks():
        listbox.insert(tkinter.END,str(book))

def addBook():
    library.addBook(titleEntry.get(), authorEntry.get())
    refresh()

def searchBook():
    book=library.findBook(titleEntry.get())
    listbox.delete(0, tkinter.END)
    if book:
        listbox.insert(tkinter.END, str(book))

def borrowBook():
    library.borrowBook(titleEntry.get())
    refresh()

def returnBook():
    library.returnBook(titleEntry.get())
    refresh()

def save():
    library.saveToFile()

tkinter.Label(window, text="Title").pack()
titleEntry.pack()
tkinter.Label(window, text="Author").pack()
authorEntry.pack()
tkinter.Button(window, text="Add", command=addBook).pack()
tkinter.Button(window, text="Search", command=searchBook).pack()
tkinter.Button(window, text="Borrow", command=borrowBook).pack()
tkinter.Button(window, text="Return", command=returnBook).pack()
tkinter.Button(window, text="Save", command=save).pack()
listbox.pack()
refresh()
window.mainloop()