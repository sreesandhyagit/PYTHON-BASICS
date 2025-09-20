from abc import ABC, abstractmethod


# ✅ Decorator for logging actions
def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"\n[LOG] Executing: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


# ✅ Abstract Class
class User(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display_info(self):
        pass


# ✅ Book Class with Encapsulation
class Book:
    def __init__(self, title, author, copies=1):
        self.title = title
        self.author = author
        self.__copies = copies  # Private attribute

    def is_available(self):
        return self.__copies > 0

    def borrow(self):
        if self.is_available():
            self.__copies -= 1
            return True
        return False

    def return_book(self):
        self.__copies += 1

    def get_copies(self):
        return self.__copies

    def __str__(self):
        return f"{self.title} by {self.author} ({self.__copies} copies available)"


# ✅ Member class (Inheritance from User)
class Member(User):
    member_count = 0  # Class variable

    def __init__(self, name):
        super().__init__(name)
        self.borrowed_books = []
        Member.member_count += 1

    @log_action
    def borrow_book(self, book: Book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is currently unavailable.")

    @log_action
    def return_book(self, book: Book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} has not borrowed '{book.title}'")

    def display_info(self):  # Polymorphism
        print(f"Member: {self.name}")
        if self.borrowed_books:
            print("Borrowed books:")
            for book in self.borrowed_books:
                print(f" - {book.title}")
        else:
            print("No books borrowed.")

    @classmethod
    def total_members(cls):
        return cls.member_count

    @staticmethod
    def validate_name(name):
        return name.strip() != ""


# ✅ Library Class
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    @log_action
    def add_book(self, book: Book):
        for b in self.books:
            if b.title.lower() == book.title.lower() and b.author.lower() == book.author.lower():
                b.return_book()  # Increase count
                print(f"Added another copy of '{b.title}'")
                return
        self.books.append(book)
        print(f"Added new book '{book.title}'")

    def display_books(self):
        print(f"\nBooks in {self.name}:")
        if not self.books:
            print("No books available.")
        for book in self.books:
            print(f" - {book}")

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None


# ✅ Menu-Driven App
def main():
    library = Library("Central Library")
    members = {}

    while True:
        print("\n========== Library Menu ==========")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Display All Books")
        print("6. Display Member Info")
        print("7. Show Total Members")
        print("0. Exit")
        print("==================================")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author: ")
            copies = int(input("Enter number of copies: "))
            library.add_book(Book(title, author, copies))

        elif choice == '2':
            name = input("Enter member name: ")
            if Member.validate_name(name):
                members[name] = Member(name)
                print(f"Member '{name}' registered.")
            else:
                print("Invalid name.")

        elif choice == '3':
            name = input("Enter member name: ")
            title = input("Enter book title: ")
            member = members.get(name)
            book = library.find_book(title)
            if member and book:
                member.borrow_book(book)
            else:
                print("Member or book not found.")

        elif choice == '4':
            name = input("Enter member name: ")
            title = input("Enter book title: ")
            member = members.get(name)
            book = library.find_book(title)
            if member and book:
                member.return_book(book)
            else:
                print("Member or book not found.")

        elif choice == '5':
            library.display_books()

        elif choice == '6':
            name = input("Enter member name: ")
            member = members.get(name)
            if member:
                member.display_info()
            else:
                print("Member not found.")

        elif choice == '7':
            print(f"Total registered members: {Member.total_members()}")

        elif choice == '0':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


# ✅ Run program
if __name__ == "__main__":
    main()
