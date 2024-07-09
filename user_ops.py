class Users:
    def __init__(self, name, library_id, books_checked_out):
        self.name = name
        self._library_id = library_id
        self.books_checked_out = books_checked_out

def user_menu():
    print("User Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")
    print("4. Quit to previous menu")

