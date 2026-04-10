class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"'{self.title}' by {self.author}")

my_book = Book("The Great Gatsby", "F. Scott Fitzgerald")
my_book.display()
