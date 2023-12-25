class Library():
    def _init_(self,title,author,item_no):
        self.title = title
        self.author = author
        self.item_id = item_no
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Item ID: {self.item_id}")


class Book(Library):

    def _init_(self, title, author, item_no, num_pages):
        super()._init_(title, author, item_no)
        self.num_pages = num_pages
        
    def display_info(self):
        super().display_info()
        print(f"Number of Pages: {self.num_pages}")
        
class Dvd(Library):
    def _init_(self, title, director, item_no, duration):
        super()._init_(title, director, item_no)
        self.director = director
        self.duration = duration
    def display_info(self):
     super().display_info()
     print(f"Director: {self.director}")
     print(f"Duration: {self.duration} minutes")
class Journal(Library):
    def _init_(self, title, publisher, item_id, issue_number):
        super()._init_(title, publisher, item_id)
        self.publisher = publisher
        self.issue_number = issue_number

    def display_info(self):
        super().display_info()
        print(f"Publisher: {self.publisher}")
        print(f"Issue Number: {self.issue_number}")


book1 = Book("The liliput", "idk", "1", 180)
dvd1 = Dvd("Inception", "Christopher Nolan", "1", 148)
journal1 = Journal("National Geographic", "National Geographic Society", "1", 123)

book1.display_info()
dvd1.display_info()
journal1.display_info()