from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """

def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Unknown command. Please try again. ")

        user_input = input(USER_CHOICE)


# ask for book name and author
def prompt_add_book():
    name = input('Enter the new book name: ')
    author = input('Enter the new book author: ')
    database.add_book(name, author)


# show all the books in out list
def list_books():
    books = database.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'        # 'YES' if book[read] == True else 'NO'
        # read = 'YES' if book['read'] == '1' else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")


# ask for book name and change it to read in our list
def prompt_read_book():
    name = input('Enter the name of the book you just finished reading: ')
    database.mark_book_as_read(name)


# ask for book name and remove book from list
def prompt_delete_book():
    name = input('Enter the name of the book you wish to delete: ')
    database.delete_book(name)


menu()