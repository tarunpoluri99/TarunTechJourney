''' Q6. Create a class Book with:
•	instance attributes title, author
•	a class variable total_books
•	a class method from_string(cls, book_str) that creates an object from "title-author" format
•	a static method is_valid_title(title) that checks if title has at least 3 characters
•	increment total_books for every book created '''
class Book:
    total_books=0
    def __init__(self,title,author):
        self.title=title
        self.author=author
        Book.total_books+=1
    @classmethod
    def from_string(cls,book_str):
        title,author=book_str.split("-")
        return cls(title,author)

    @staticmethod
    def is_valid_title(title):
        return len(title)>3
# using CM()-> from_string() bcuz the below the string contains title and author in 1 string

b1=Book.from_string("DREAM-Tarun")
print("Title: ",b1.title)
print("Author: ",b1.author)

# normal obj creation without using CM() bcuz title and author is given in seperte parameters
b2=Book("Hope","Kiran")

# Validating the title SM()-> is_valid_title using objects
print(b1.is_valid_title(b1.title))
print(b2.is_valid_title(b2.title))
print()
# Validating the title SM()-> is_valid_title using objects
print(Book.is_valid_title(b1.title))
print(Book.is_valid_title(b2.title))

print(Book.total_books)


