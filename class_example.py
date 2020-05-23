from operator import attrgetter


class Page:
    book_title = 'Python Practice Book'

    def __init__(self, num, content):
        self.num = num
        self.content = content

    def output(self):
        return f'{self.content}'

    @classmethod
    def print_pages(cls, *pages):
        print(cls.book_title)
        pages = list(pages)
        for page in sorted(pages, key=attrgetter('num')):
            print(page.output())


title_page = Page(0, 'title page')
# print(type(title_page))
# print(isinstance(title_page, Page))
# print(dir(title_page))
# print(title_page.output())

first = Page(1, 'first page')
second = Page(2, 'second page')
third = Page(3, 'third page')
# print(first_page.output())
Page.print_pages(first, second, third)
first.print_pages(first, second, third)


class Book:

    def __init__(self, raw_price):
        if raw_price < 0:
            raise ValueError('Price must be positive')
        self.raw_price = raw_price
        self._discounts = 0

    @property
    def discounts(self):
        return self._discounts

    @discounts.setter
    def discounts(self, value):
        if value < 0 or 100 < value:
            raise ValueError('discounts must be between 0 and 100')
        self._discounts = value

    @property
    def price(self):
        multi = 100 - self._discounts
        return int(self.raw_price * multi / 100)

book = Book(2000)
print(book.discounts)
print(book.price)
book.discounts = 20
print(book.price)
# book.discounts = 120
