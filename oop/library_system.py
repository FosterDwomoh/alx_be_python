class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"Book: {self.title} by {self.author}"
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    def __str__(self):
        return f"EBook: {self.title} by {self.author} file_size: {self.file_size}"
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
    def __str__(self):
        return f"PrintBook: {self.title} by {author} page_count: {page_count}"
class library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def list_books(self)
    for book in self.books:
        if isinstance(book, EBook):
            print(f"EBook: {book.title} by {book.author}, file size: {book.file_size}")
        elif isinstance(book, PrintBook):
            print(f"PrintBook: {book.title} by {book.author}, page count: {book.page_count}")
        elif isinstance(book, Book):
            print(f"Book: {book.title} by {book.author}")
    def main:
        classic_book = Book("Pride and Prejudice", "Jane Austen")
        digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
        paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)
        my_library.add_book(classic_book)
        my_library.add_book(digital_novel)
        my_library.add_book(paper_novel)
        my_library.list_books()
    if __name__=="__main__":
        main()
