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
        pass

    def get_title(self):
        pass

    def get_isbn(self):
        pass

    def add_rating(self, rating):
        pass

    def __eq__(self, other_book):
        pass

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__()
        pass

    def get_author(self):
        pass

    def __repr__(self):
        pass


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
    user1 = User('karel', 'karel@kareldegroot.mail')
    print(user1)

