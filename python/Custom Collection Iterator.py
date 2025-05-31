from abc import ABC, abstractmethod
from typing import List, Optional, Dict
from enum import Enum, auto

class Book:
    def __init__(self, title: str, author: str, category: str):
        self.title = title
        self.author = author
        self.category = category
    
    def __str__(self):
        return f"'{self.title}' by {self.author} [{self.category}]"

class IteratorStrategy(Enum):
    DEFAULT = auto()
    BY_AUTHOR = auto()
    BY_CATEGORY = auto()
    REVERSE = auto()

class BookIterator(ABC):
    @abstractmethod
    def __iter__(self):
        pass
    
    @abstractmethod
    def __next__(self) -> Book:
        pass

class DefaultIterator(BookIterator):
    def __init__(self, books: List[Book]):
        self._books = books
        self._index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self) -> Book:
        if self._index < len(self._books):
            book = self._books[self._index]
            self._index += 1
            return book
        raise StopIteration

class AuthorIterator(BookIterator):
    def __init__(self, books: List[Book], author: str):
        self._books = [b for b in books if b.author == author]
        self._index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self) -> Book:
        if self._index < len(self._books):
            book = self._books[self._index]
            self._index += 1
            return book
        raise StopIteration

class CategoryIterator(BookIterator):
    def __init__(self, books: List[Book], category: str):
        self._books = [b for b in books if b.category == category]
        self._index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self) -> Book:
        if self._index < len(self._books):
            book = self._books[self._index]
            self._index += 1
            return book
        raise StopIteration

class ReverseIterator(BookIterator):
    def __init__(self, books: List[Book]):
        self._books = books[::-1]
        self._index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self) -> Book:
        if self._index < len(self._books):
            book = self._books[self._index]
            self._index += 1
            return book
        raise StopIteration

class BookCollection:
    def __init__(self, iterator_factory=None):
        self._books: List[Book] = []
        self._iterator_factory = iterator_factory or DefaultIterator
    
    def add_book(self, book: Book) -> None:
        self._books.append(book)
    
    def get_books(self) -> List[Book]:
        return self._books.copy()
    
    def __iter__(self):
        return self._iterator_factory(self._books)
    
    def create_iterator(self, strategy: IteratorStrategy = IteratorStrategy.DEFAULT, 
                       filter_value: Optional[str] = None) -> BookIterator:
        if strategy == IteratorStrategy.BY_AUTHOR:
            if not filter_value:
                raise ValueError("Author name required for BY_AUTHOR strategy")
            return AuthorIterator(self._books, filter_value)
        elif strategy == IteratorStrategy.BY_CATEGORY:
            if not filter_value:
                raise ValueError("Category required for BY_CATEGORY strategy")
            return CategoryIterator(self._books, filter_value)
        elif strategy == IteratorStrategy.REVERSE:
            return ReverseIterator(self._books)
        else:
            return DefaultIterator(self._books)

def main():
    collection = BookCollection()
    
    collection.add_book(Book("1984", "George Orwell", "Dystopia"))
    collection.add_book(Book("Animal Farm", "George Orwell", "Satire"))
    collection.add_book(Book("The Hobbit", "J.R.R. Tolkien", "Fantasy"))
    collection.add_book(Book("Clean Code", "Robert C. Martin", "Programming"))
    collection.add_book(Book("The Clean Coder", "Robert C. Martin", "Programming"))
    
    print("=== Default Iteration ===")
    for book in collection:
        print(book)
    
    print("\n=== Books by George Orwell ===")
    orwell_books = collection.create_iterator(
        strategy=IteratorStrategy.BY_AUTHOR,
        filter_value="George Orwell"
    )
    for book in orwell_books:
        print(book)
    
    print("\n=== Programming Books ===")
    programming_books = collection.create_iterator(
        strategy=IteratorStrategy.BY_CATEGORY,
        filter_value="Programming"
    )
    for book in programming_books:
        print(book)
    
    print("\n=== Reverse Order ===")
    reverse_iter = collection.create_iterator(strategy=IteratorStrategy.REVERSE)
    for book in reverse_iter:
        print(book)

if __name__ == "__main__":
    main()