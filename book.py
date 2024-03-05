class Book:
    def __init__(self, title, author, isbn):
        self._title = title
        self._author = author
        self._isbn = isbn

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author
    
    @property
    def isbn(self):
        return self._isbn
    
    @title.setter
    def title(self, t):
        self._title = t

    @author.setter
    def author(self, a):
        self._author = a

    @isbn.setter
    def isbn(self, i):
        self._isbn = i
    
    def get_details(self):
        return [self.title, self.author, self.isbn]

