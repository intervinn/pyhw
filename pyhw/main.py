import datetime
from item import Item
from book import Book

b = Book("name", datetime.datetime(year=2023, month=5, day=2), "books.co", "fantasy", "k.s. sasws", 1000)
b.name = "hi"
print(b.name)
b.print_data()

