from abc import ABC, abstractmethod

class Items(ABC):
    def __init__(self, title, author):
        self._title = title
        self._author = author
        self.__available =True

    @abstractmethod
    def display(self):
        pass

    def isAvailable(self):
        return self.__available

    def borrow_item(self):
        if self.__available:
            self.__available = False
            print(f"'{self._title}' is borrowed successfully!")
        else:
            print(f"'{self._title}' is not available!!")
    
    def return_item(self):
        self.__available = True
        print(f"'{self._title}' is returned successfully!")


class Book(Items):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages
    
    def display(self):
        print(f"Book : {self._title} by {self._author}, {self.pages} pages.")

class Magazine(Items):
    def __init__(self, title, author, issue):
        super().__init__(title, author)
        self.issue = issue
    
    def display(self):
        print(f"Magazine : {self._title} by {self._author}, Issue : {self.issue}.")


class Library:
    totalItems = 0
  
    def __init__(self, name):
        self.lib_name = name
        self.lib_items = []
        Library.totalItems = 0
  
    def addItems(self, item):
        self.lib_items.append(item)
        Library.totalItems += 1

    def __add__(self,other):
        new_library =Library(self.lib_name + " & " + other.lib_name)
        new_library.lib_items = self.lib_items + other.lib_items
        Library.totalItems = len(new_library.lib_items)
        return new_library

    @classmethod
    def get_total_items(cls):
        return cls.totalItems

    @staticmethod
    def Library_Info():
        print("******A Library - Wide Storage of Books and Magazines for Readers*******")


Library.Library_Info()
lib1 = Library("Central Library")
lib2 = Library("Town Library")
lib3 = Library("City Library")

b1 = Book("Python OOP","John Doe",350)
b2 = Book("Data Science", "Alice", 420)
b3 = Book("C++ Programming","Sumitha Arora",300)
m1 = Magazine("Tech Today", "Editor X", "Sep 2025")
m2 = Magazine("Info Kairali","Team Info","Sep 2025")
m3 = Magazine("Tech Media","ABCD","January 2024")

lib1.addItems(b1)
lib1.addItems(b2)
lib1.addItems(m1)

lib2.addItems(b2)
lib2.addItems(m2)

lib3.addItems(b3)
lib3.addItems(m3)

print("\n-----------Items in Central Library----------")
for item in lib1.lib_items:
    item.display()

print("\n-----------Items in Town Library----------")
for item in lib2.lib_items:
    item.display()

print("\n-----------Items in City Library----------")
for item in lib3.lib_items:
    item.display()


print(f"\nBorrow & Return Items in {lib1.lib_name}")
b1.borrow_item()
b1.borrow_item()
b1.return_item()

print(f"\nTotal items in {lib1.lib_name} : {len(lib1.lib_items)}")
print(f"Total items in {lib2.lib_name} : {len(lib2.lib_items)}")
print(f"Total items in {lib3.lib_name} : {len(lib3.lib_items)}")

merged_library = lib1 + lib2 + lib3
print("\nMerged Library : ",merged_library.lib_name)
print(f"Total items in merged library: ",Library.get_total_items())

print("\nTotal items across libraries:",len(lib1.lib_items)+len(lib2.lib_items)+len(lib3.lib_items) )









