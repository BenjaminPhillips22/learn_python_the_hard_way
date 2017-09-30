# Class Inheritance


class Book:
    booksAreCool = True

    def __init__(self, pages, author):
        self.pages = pages
        self.author = author
        print("Calling Book constructor")

    def bookMethod(self):
        print("Calling book method")


class Ebook(Book):
    def __init__(self, pages, author):
        self.pages = pages
        self.author = author
        print("Calling Ebook constructor")

    def ebookMethod(self):
        print("Calling ebook method")


e = Ebook(pages=10, author='Ben')

e.bookMethod()
e.ebookMethod()
e.__setattr__('booksAreCool', False)
print(e.booksAreCool)

# checking for classes and subclasses

if issubclass(Ebook, Book):
    print(f"{Ebook.__name__} is a subclass of {Book.__name__}")

if isinstance(e, Book):
    print(f"{e.__class__} is an instance of {Book.__name__}")
