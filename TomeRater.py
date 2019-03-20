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

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        total = 0
        count = 0
        for book,rate in self.books.items():
            if rate:
                total += rate
                count += 1
        return total/count

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
        print("The isbn for '{book}', has been updated to {isbn}.".format(book=self.title, isbn=self.isbn))

    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return "These books are the same!"

    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_average(self):
        if len(self.ratings) >= 1:
            return sum(self.ratings) / len(self.ratings)

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)


class Non_Fiction(Book):
    def __init__(self, subject, title, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)

class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if self.users[email]:
            self.users[email].read_book(book, rating)
            if rating:
                book.add_rating(rating)
            if self.books.get(book):
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            return "No user with email {email}!".format(email=email)

    def add_user(self, name, email, user_books=None):
        self.users[email] = User(name, email)
        if user_books:
            for book in user_books:
                self.add_book_to_user(book, email, book.get_average())

    # Analysis methods
    def print_catalog(self):
        for key, value in self.books.items():
            print(key)

    def print_users(self):
        for key, value in self.users.items():
            print(value)

    def most_read_book(self):
        return max(self.books, key=self.books.get)

    def highest_rated_book(self):
        highest_book = 0
        highest_value = 0
        for key, value in self.books.items():
            current = key.get_average()
            if current > highest_value:
                highest_value = current
                highest_book = key
        return highest_book

    def most_positive_user(self):
        positive_user = 0
        positivest_rating = 0
        for key, value in self.users.items():
            current = value.get_average_rating()
            if current > positivest_rating:
                positivest_rating = current
                positive_user = value
        return positive_user


if __name__ == "__main__":
    # Testing user class
    user1 = User('karel', 'karel@kareldegroot.mail')
    print(user1)
    user2 = User('karel', 'karel@kareldegroot.mail')
    # users should be equal
    print(user1 == user2)
    # Change user2 email, so they won't be equal anymore.
    print(user2.get_email())
    user2.change_email('niet@kareldegroot.nl')
    print(user2.get_email())

    # Testing book class
    book1 = Book('I am a book', 178236217863)
    book2 = Book('I am a book', 178236217863)
    print(book1 == book2)
    print(book1.get_title())
    print(book1.get_isbn())
    #change isbn
    book1.set_isbn(109238901238)
    book1.add_rating(1)
    book1.add_rating(5)
    book1.add_rating(3)
    print(book1.ratings)

    # Test Fiction class
    fiction1 = Fiction("Alice In Wonderland", "Lewis Carroll", 981237123)
    print(fiction1.get_isbn())
    print(fiction1.get_author())
    print(fiction1.get_title())
    print(fiction1)

    # Test Non_Fiction class
    non_fiction1 = Non_Fiction("Society of Mind", "Artificial Intelligence", "beginner", 3456787654)
    print(non_fiction1)
    print(non_fiction1.get_title())
    print(non_fiction1.get_subject())
    print(non_fiction1.get_level())

    # Testing User read_book and get_average
    print(user1)
    user1.read_book(book1)
    user1.read_book(book2, 5)
    print(user1)
    print(user1.get_average_rating())
    user1.read_book(book1, 3)
    user1.read_book(book2, 5)
    print(user1)
    print(user1.get_average_rating())

    #Tome_Rater.add_book_to_user(book1, "niet@kareldegroot.nl", 1)

    # Testing Book get_average
    print(book1.ratings)
    print(book1.get_average())
    book1.add_rating(1)
    book1.add_rating(4)
    book1.add_rating(3)
    book1.add_rating(2)
    book1.add_rating(3)
    print(book1.ratings)
    print(book1.get_average())

    #Tome_Rater = TomeRater()

    #Create some books:
    book1 = Tome_Rater.create_book("Society of Mind", 12345678)
    novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
    novel1.set_isbn(9781536831139)
    nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
    nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
    novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
    novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

    #Create users:
    Tome_Rater.add_user("Alan Turing", "alan@turing.com")
    Tome_Rater.add_user("David Marr", "david@computation.org")

    #Add a user with three books already read:
    Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

    #Add books to a user one by one, with ratings:
    Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
    Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
    Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
    Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
    Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

    Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
    Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
    Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)

    #Uncomment these to test your functions:
    Tome_Rater.print_catalog()
    Tome_Rater.print_users()

    print("Most positive user:")
    print(Tome_Rater.most_positive_user())
    print("Highest rated book:")
    print(Tome_Rater.highest_rated_book())
    print("Most read book:")
    print(Tome_Rater.most_read_book())
