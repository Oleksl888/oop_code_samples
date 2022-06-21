'''Создайте класс, описывающий книгу. Он должен содержать информацию об авторе, названии, годе
издания и жанре. Создайте несколько разных книг. Определите для него операции проверки на
равенство и неравенство, методы __repr__ и __str__.'''


class Book():
    def __init__(self, author, name, year, genre):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre

    def __repr__(self):
        return f'<Book (Author:{self.author}, Name:{self.name}, Year:{self.year}, Genre:{self.genre})>'

    def __str__(self):
        return f'''
{self.name} by {self.author}
{self.genre}, {self.year}'''

    def __eq__(self, other):
        return self.author == other.author and self.name == other.name and \
               self.genre == other.genre and self.year == other.year

    def __ne__(self, other):
        return self.author != other.author or self.name != other.name or \
               self.genre != other.genre or self.year != other.year


if __name__ == '__main__':
    book1 = Book('Wells', 'Time Machine', 1857, 'science fiction')
    book2 = Book('Orwell', '1984', 1930, 'dystopia')
    book3 = Book('Wells', 'Time Machine', 1857, 'science fiction')
    print(book1)
    print(repr(book2))
    print(book1 == book2)
    print(book1 != book2)
    print(book1 == book3)
    print(book1 != book3)
