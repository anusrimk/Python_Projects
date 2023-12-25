#Design a library catalogue system using inheritance. take base class library item
# and  classes book, dvd and journal. each derived class should have unique attributes
# and methods and system should support checking in and checking out System. Use 
# hierarchal inheritance  and there should be a counter variable, the attributes for books
# should be same, title author books id


# class LibraryItem:
#     counter = 1

#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.item_id = LibraryItem.counter
#         LibraryItem.counter += 1
#         self.checked_out = False

#     def display_info(self):
#         print(f"Item ID: {self.item_id}")
#         print(f"Title: {self.title}")
#         print(f"Author: {self.author}")
#         print(f"Status: {'Checked out' if self.checked_out else 'Available'}")

#     def check_out(self):
#         if not self.checked_out:
#             print("Item checked out successfully.")
#             self.checked_out = True
#         else:
#             print("Item is already checked out.")

#     def check_in(self):
#         if self.checked_out:
#             print("Item checked in successfully.")
#             self.checked_out = False
#         else:
#             print("Item is already checked in.")

# class Book(LibraryItem):
#     def __init__(self, title, author, genre):
#         super().__init__(title, author)
#         self.genre = genre

#     def display_info(self):
#         super().display_info()
#         print(f"Genre: {self.genre}")


# class DVD(LibraryItem):
#     def __init__(self, title, director, duration):
#         super().__init__(title, director)
#         self.director = director
#         self.duration = duration

#     def display_info(self):
#         super().display_info()
#         print(f"Director: {self.director}")
#         print(f"Duration: {self.duration} minutes")


# class Journal(LibraryItem):
#     def __init__(self, title, author, issue_number):
#         super().__init__(title, author)
#         self.issue_number = issue_number

#     def display_info(self):
#         super().display_info()
#         print(f"Issue Number: {self.issue_number}")


# def display_menu(items):
#     print("0. Exit")
#     for item in items:
#         print(f"{item.item_id}. Display {type(item).__name__} Information")
#     print("99. Check Out an Item")
#     print("98. Check In an Item")


# def choose_action():
#     return int(input("Enter your choice: "))


# def check_out_item(item):
#     if not item.checked_out:
#         print(f"{type(item).__name__} checked out successfully.")
#         item.checked_out = True
#     else:
#         print(f"{type(item).__name__} is already checked out.")


# def check_in_item(item):
#     if item.checked_out:
#         print(f"{type(item).__name__} checked in successfully.")
#         item.checked_out = False
#     else:
#         print(f"{type(item).__name__} is already checked in.")


# # Example usage:

# book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction")
# dvd1 = DVD("Inception", "Christopher Nolan", 148)
# journal1 = Journal("Scientific American", "Various Authors", 123)

# items = [book1, dvd1, journal1]

# while True:
#     display_menu(items)
#     choice = choose_action()

#     if choice == 0:
#         break
#     elif choice == 99:
#         item_id = int(input("Enter Item ID to check out: "))
#         selected_item = next((item for item in items if item.item_id == item_id), None)
#         if selected_item:
#             check_out_item(selected_item)
#         else:
#             print("Invalid Item ID")
#     elif choice == 98:
#         item_id = int(input("Enter Item ID to check in: "))
#         selected_item = next((item for item in items if item.item_id == item_id), None)
#         if selected_item:
#             check_in_item(selected_item)
#         else:
#             print("Invalid Item ID")
#     elif 1 <= choice <= len(items):
#         items[choice - 1].display_info()
#     else:
#         print("Invalid choice. Please enter a valid option.")


class LibraryItem:
    counter = 1

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.item_id = LibraryItem.counter
        LibraryItem.counter += 1
        self.checked_out = False

    def display_info(self):
        print(f"Item ID: {self.item_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {'Checked out' if self.checked_out else 'Available'}")

    def check_out(self):
        if not self.checked_out:
            print("Item checked out successfully.")
            self.checked_out = True
        else:
            print("Item is already checked out.")

    def check_in(self):
        if self.checked_out:
            print("Item checked in successfully.")
            self.checked_out = False
        else:
            print("Item is already checked in.")


class Book(LibraryItem):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre

    def display_info(self):
        super().display_info()
        print(f"Genre: {self.genre}")


class DVD(LibraryItem):
    def __init__(self, title, director, duration):
        super().__init__(title, director)
        self.director = director
        self.duration = duration

    def display_info(self):
        super().display_info()
        print(f"Director: {self.director}")
        print(f"Duration: {self.duration} minutes")


class Journal(LibraryItem):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number

    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.issue_number}")


def display_menu():
    print("1. Display Book Information")
    print("2. Display DVD Information")
    print("3. Display Journal Information")
    print("4. Check Out an Item")
    print("5. Check In an Item")
    print("0. Exit")


def choose_action():
    return int(input("Enter your choice (0-5): "))



book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction")
dvd1 = DVD("Inception", "Christopher Nolan", 148)
journal1 = Journal("Scientific American", "Various Authors", 123)

while True:
    display_menu()
    choice = choose_action()

    if choice == 0:
        break
    elif choice == 1:
        book1.display_info()
    elif choice == 2:
        dvd1.display_info()
    elif choice == 3:
        journal1.display_info()
    elif choice == 4:
        item_id = int(input("Enter Item ID to check out: "))
        if item_id == book1.item_id:
            book1.check_out()
        elif item_id == dvd1.item_id:
            dvd1.check_out()
        elif item_id == journal1.item_id:
            journal1.check_out()
        else:
            print("Invalid Item ID")
    elif choice == 5:
        item_id = int(input("Enter Item ID to check in: "))
        if item_id == book1.item_id:
            book1.check_in()
        elif item_id == dvd1.item_id:
            dvd1.check_in()
        elif item_id == journal1.item_id:
            journal1.check_in()
        else:
            print("Invalid Item ID")
    else:
        print("Invalid choice. Please enter a number between 0 and 5.")



# class LibraryItem:
#     def _init_(self, title, author, item_id):
#         self.title = title
#         self.author = author
#         self.item_id = item_id
#         self.checked_out = False

#     def display_info(self):
#         print("Title:",self.title)
#         print("Author:",self.author)
#         print("Item ID:",self.item_id)
#         print("Status: Checked out" if self.checked_out else "Status: Available")

#     def check_out(self):
#         if not self.checked_out:
#             self.checked_out = True
#             print(self.title, "checked out successfully.")
#         else:
#             print(self.title, "is already checked out.")

#     def check_in(self):
#         if self.checked_out:
#             self.checked_out = False
#             print(self.title, "checked in successfully.")
#         else:
#             print(self.title, "is not checked out.")


# class Book(LibraryItem):
#     def _init_(self, title, author, item_id, genre):
#         super()._init_(title, author, item_id)
#         self.genre = genre

#     def display_info(self):
#         super().display_info()
#         print("Genre:",self.genre)


# class DVD(LibraryItem):
#     def _init_(self, title, director, item_id, duration):
#         super()._init_(title, director, item_id)
#         self.director = director
#         self.duration = duration

#     def display_info(self):
#         super().display_info()
#         print("Director:",self.director)
#         print("Duration:",self.duration, "minutes")


# class Journal(LibraryItem):
#     def _init_(self, title, publisher, item_id, issue_number):
#         super()._init_(title, publisher, item_id)
#         self.publisher = publisher
#         self.issue_number = issue_number

#     def display_info(self):
#         super().display_info()
#         print("Publisher:",self.publisher)
#         print("Issue Number:",self.issue_number)


# def create_library_item():
#     item_type = input("Enter the type of item (Book/DVD/Journal): ").lower()
#     title = input("Enter the title: ")
#     author_director_publisher = input("Enter the author/director/publisher: ")
#     item_id = input("Enter the item ID: ")

#     if item_type == "book":
#         genre = input("Enter the genre: ")
#         return Book(title, author_director_publisher, item_id, genre)
#     elif item_type == "dvd":
#         duration = input("Enter the duration (in minutes): ")
#         return DVD(title, author_director_publisher, item_id, duration)
#     elif item_type == "journal":
#         issue_number = input("Enter the issue number: ")
#         return Journal(title, author_director_publisher, item_id, issue_number)
#     else:
#         print("Invalid item type. Returning None.")
#         return None


# # Example Usage
# library_items = []

# while True:
#     print("\n1. Add Item\n2. Check Out\n3. Check In\n4. Display Catalogue\n5. Exit")
#     choice = input("Enter your choice (1-5): ")

#     if choice == '1':
#         new_item = create_library_item()
#         if new_item:
#             library_items.append(new_item)
#             print("Item added to the library.")

#     elif choice == '2':
#         item_id = input("Enter the item ID to check out: ")
#         for item in library_items:
#             if item.item_id == item_id:
#                 item.check_out()
#                 break
#         else:
#             print("Item not found in the library.")

#     elif choice == '3':
#         item_id = input("Enter the item ID to check in: ")
#         for item in library_items:
#             if item.item_id == item_id:
#                 item.check_in()
#                 break
#         else:
#             print("Item not found in the library.")

#     elif choice == '4':
#         print("\nLibrary Catalogue:")
#         for item in library_items:
#             item.display_info()

#     elif choice == '5':
#         print("Exiting program.")
#         break

#     else:
#         print("Invalid choice. Please enter a number between 1 and 5.")