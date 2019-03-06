class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("The email for {user} has been changed to {newmail}.".format(user=self.name, newmail=address))

    def __repr__(self):
        return "User {user}, email: {email}, books read: {books}".format(user=self.name, email=self.email, books=len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return "These users are the same!"


class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("The isbn for {book}, has been updated to {isbn}.".format(book=self.title, isbn=self.isbn))

    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return "These books are the same!"

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__()
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)


class Non_Fiction(Book):
    def __init__(self, subject, title, leven):
        super().__init__()
        pass

    def get_subject(self):
        pass

    def get_level(self):
        pass

    def __repr__(self):
        pass

if __name__ == "__main__":
    # Testing user class
    user1 = User('karel', 'karel@kareldegroot.mail')
    print(user1)
    user2 = User('karel', 'karel@kareldegroot.mail')
    # users should be equal
    print(user1 == user2)
    # Change user2 email, so they won't be equal anymore.
    user2.change_email('niet@kareldegroot.nl')

    # Testing book class
    book1 = Book('I am a book', 178236217863)
    book2 = Book('I am a book', 178236217863)
    print(book1 == book2)
    book1.get_title()
    book1.get_isbn()
    #change isbn
    book1.set_isbn(109238901238)
    book1.add_rating(1)
    book1.add_rating(5)
    book1.add_rating(3)
    print(book1.ratings)

    # Test Fiction class

