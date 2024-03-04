from book import Book
from user import User

class Storage():
    
    def __init__(self):
        self.books = []
        self.users = []
        self.checkouts = []

    def store_books_from_csv(self, csv_filename):
        try:
            with open(csv_filename, 'r') as file:
                line = file.readline()
                while line:
                    data = line.strip().split(",")
                    title = data[0]
                    author = data[1]
                    isbn = data[2]
                    self.add_book(title, author, isbn)
                    line = file.readline()
        
        except FileNotFoundError:
            print("The file "+csv_filename+" could not be found.")
        
        except Exception as e:
            print(e)
    

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)

    def list_books(self):
        format_row_others = "{:^35}|" * (3)
        print(format_row_others.format(*[i for i in ["Title", "Author", "ISBN"]]))
        print(format_row_others.format(*[i for i in ["-"*10, "-"*10, "-"*10]]))
        for book in self.books:
            print(format_row_others.format(*[i for i in book.get_details()]))

    def add_user(self, name, user_id):
        user = User(name, user_id)
        self.users.append(user)


# if __name__ == "__main__":
#     st = Storage()
#     st.store_books_from_csv("test_books.csv")
#     st.list_books()