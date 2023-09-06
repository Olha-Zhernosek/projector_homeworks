from functools import wraps

'''Create a class Product with properties name, price,
and quantity. Create a child class Book that inherits from
Product and adds a property author and a method called read
that prints information about the book.'''


def print_border(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('=' * 35)
        func(*args, **kwargs)
        print('=' * 35)
    return wrapper


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Book(Product):
    def __init__(self, name, price, quantity, author):
        self.author = author
        super().__init__(name, price, quantity)

    @print_border
    def read(self):
        print(f"Book: {self.name}")
        print(f"Author: {self.author}")
        print(f"Price: ₴ {self.price}")
        print(f"Quantity: {self.quantity}")


book_1 = Book('Dagon', 870, 25, 'Howard Phillips Lovecraft')
book_2 = Book('The Haunter of the Dark', 845, 13, 'Howard Phillips Lovecraft')

book_1.read()
book_2.read()
