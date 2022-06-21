'''Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле – список отзывов. Сделайте
так, что при выводе книги на экран при помощи функции print также будут выводиться отзывы к ней.'''


class Book:
    def __init__(self, author, name, year, genre, review = 'Very fancy book'):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre
        self.review = Reviews(name, review)

    def __repr__(self):
        return f'<Book (Author:{self.author}, Name:{self.name}, Year:{self.year}, Genre:{self.genre})>'

    def __str__(self):
        return f'''
{self.name} by {self.author}
{self.genre}, {self.year}
User Reviews: {self.review.review}'''

    def __eq__(self, other):
        return self.author == other.author and self.name == other.name and \
               self.genre == other.genre and self.year == other.year

    def __ne__(self, other):
        return self.author != other.author or self.name != other.name or \
               self.genre != other.genre or self.year != other.year

    def add_review(self, review):
        self.review.review.append(review)


class Reviews:
    def __init__(self, book_name, review):
        self.book_name = book_name
        self.review = []
        self.review.append(review)


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
    book1.add_review('Amazing, absolutely amazing')
    print(book1)
