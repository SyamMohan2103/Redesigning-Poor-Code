from book import Book
from user import User
from checkout import Checkout


class BookNFException(Exception):
    """
        Exception raised when the Book ISBN is not found.
    """
    pass


class UserNFException(Exception):
    """
        Exception raised when the User ID is not found.
    """
    pass


class Storage:

    def __init__(self):
        self.books = []
        self.users = []
        self.checkouts = []

    def store_books_from_csv(self, csv_filename):
        """
        Method to store the books details from a csv file.
        Input : String - csv filename or path
        Output : Stores the csv file data into books list
        """
        try:
            with open(csv_filename, "r") as file:
                line = file.readline()
                while line:
                    data = line.strip().split(",")
                    title = data[0].strip()
                    author = data[1].strip()
                    isbn = data[2].strip()
                    self.add_book(title, author, isbn)
                    line = file.readline()
                print("Books added.")
        except FileNotFoundError:
            print("The file " + csv_filename + " could not be found. Please try again!")

        except Exception as e:
            print("The books could not be added. Please try again!")

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)

    def list_books(self):
        """
        Method to display all the books.
        """
        format_row_books = "{:^35}|" * (3)
        print(format_row_books.format(*[i for i in ["Title", "Author", "ISBN"]]))
        print(format_row_books.format(*[i for i in ["-" * 10, "-" * 10, "-" * 10]]))
        for book in self.books:
            print(format_row_books.format(*[i for i in book.get_details()]))

    def store_users_from_csv(self, csv_filename):
        """
        Method to store the user details from a csv file.
        Input : String - csv filename or path
        Output : Stores the csv file data into users list
        """
        try:
            with open(csv_filename, "r") as file:
                line = file.readline()
                while line:
                    data = line.strip().split(",")
                    name = data[0].strip()
                    user_id = data[1].strip()
                    self.add_user(name, user_id)
                    line = file.readline()
            print("Users added.")
        except FileNotFoundError:
            print("The file " + csv_filename + " could not be found. Please try again!")

        except Exception as e:
            print("The users could not be added. Please try again!")

    def add_user(self, name, user_id):
        user = User(name, user_id)
        self.users.append(user)

    def list_users(self):
        """
        Method to display all the users.
        """
        format_row_users = "{:^35}|" * (2)
        print(format_row_users.format(*[i for i in ["Name", "User ID"]]))
        print(format_row_users.format(*[i for i in ["-" * 10, "-" * 10]]))
        for user in self.users:
            print(format_row_users.format(*[i for i in user.get_details()]))

    def check_user(self, user_id):
        try:
            for user in self.users:
                if user_id == user.user_id:
                    return True
        except UserNFException:
            print("User does not exist. Please enter correct user ID.")

    def check_book(self, isbn):
        try:
            for book in self.books:
                if isbn == book.isbn:
                    return True
        except BookNFException:
            print("Book does not exist. Please enter correct ISBN.")

    def checkout_book(self, user_id, isbn):
        """
        Method to add information related to checkouts to a list
        Params:
            user_id: user id of the person taking the book
            isbn: isbn of the book being checked out
        Return: None
        """
        book_exists = self.check_book(isbn)
        user_exists = self.check_user(user_id)
        if book_exists and user_exists:
            self.checkouts.append(Checkout(user_id, isbn))
            print("Checkout added.")
        else:
            print("User or book does not present in the library. Checkout Failed!!!")

    def list_checkouts(self):
        """
        Method to display all the books that are checked out.
        """
        format_row_checkouts = "{:^35}|" * (3)
        print(
            format_row_checkouts.format(
                *[i for i in ["User ID", "ISBN", "Checkout Time"]]
            )
        )
        print(format_row_checkouts.format(*[i for i in ["-" * 10, "-" * 10, "-" * 10]]))
        for checkout in self.checkouts:
            print(format_row_checkouts.format(*[i for i in checkout.get_details()]))


# if __name__ == "__main__":
#     st = Storage()
#     st.store_books_from_csv("test_books.csv")
#     st.list_books()
#     st.check_book("978-0201896831")
