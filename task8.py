class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    

class Library(Book):
    def __init__(self, books):
        self.books = books
    
    def __len__(self):
        return len(self.books)
    
    def __getitem__(self, index):
        return self.books[index]


b1 = Book("Title1", "Author1")
b2 = Book("Title2", "Author2")
b3 = Book("Title3", "Author3")

library = Library([b1, b2, b3])
print(len(library))

print(library[0])
print(library[1])
print(library[2])
