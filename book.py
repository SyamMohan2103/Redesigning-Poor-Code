class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def get_details(self):
        return [self.title, self.author, self.isbn]

