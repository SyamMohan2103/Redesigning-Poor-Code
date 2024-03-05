# This is a deliberately poorly implemented main script for a Library Management System.

from storage import Storage

def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Add User")
    print("4. List Users")
    print("5. Checkout Book")
    print("6. Add books from csv file")
    print("7. Add users from csv file")
    print("8. Print checkout details")
    print("9. Exit")
    choice = input("Enter choice: ")
    return choice


def main():
    st = Storage()
    while True:
        choice = main_menu()
        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            st.add_book(title, author, isbn)
            print("Book added.")
        elif choice == "2":
            st.list_books()
        elif choice == "3":
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            st.add_user(name, user_id)
            print("User added.")
        elif choice == "4":
            st.list_users()
        elif choice == "5":
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            st.checkout_book(user_id, isbn)
        elif choice == "6":
            csv_filename = input("Enter csv file path: ")
            st.store_books_from_csv(csv_filename)
        elif choice == "7":
            csv_filename = input("Enter csv file path: ")
            st.store_users_from_csv(csv_filename)
        elif choice == "8":
            st.list_checkouts()
        elif choice == "9":
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
