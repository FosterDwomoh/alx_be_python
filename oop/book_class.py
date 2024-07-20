class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        del __del__(self):
            print(f"Deleting {self.title}")
            del __str__(self):
                return f"{self.title} by {self.author}, published in {self.year}"
            del __repr__(self):
                return f"Book('{self.title}', '{self.author}, published in {self.year}"
            if __name__ == "__main__"
            my_book = Book("1984" "George Orwell", 1949)
            print(str(my_book))
            print(repr(my_book))

