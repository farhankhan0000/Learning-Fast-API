from fastapi import FastAPI, Body
from typing import Optional
from pydantic import BaseModel, Field

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    rating: int
    published_year: int
    review: str

    def __init__(self, id, title, author, rating, published_year, review):
        self.id = id
        self.title = title
        self.author = author
        self.rating = rating 
        self.published_year = published_year
        self.review = review

class book_request(BaseModel):
    id: Optional[int] = Field(description= "Id is not needed when creating", default=None)
    title: str = Field(min_lenght= 2, max_length= 200)
    author: str = Field(min_length= 2, max_length= 200)
    rating: int = Field(gt=0, lt=6)
    published_year: int = Field(gt= 1800, lt= 2026)
    review: str = Field(min_length= 5, max_length= 500)

    model_config = {
        "json_schema_extra" : {
            "title" : "A New Book",
            "author" : "author name",
            "rating" : 5,
            "published_year" : 1801,
            "review" : "It was such a wonderful book"
        }
    }


Book_store = [Book(1, "Metamorphosis", "Franz Kafka", 4, 1915, "Fragility of Human Identity"),
              Book(2, "12 Rules For Life", "Jordan B Peterson", 4, 2018, "Mix of Philosophy Human Phsycology"),
              Book(3, "The Trial", "Franz Kafka", 3, 1925, "Didnt click much"),
              Book(4, "Think and Grow Rich", "Napolean Hill", 4, 1937, "Good Book with Good principles"),
              Book(5, "Crushing it", "Gary Vaynerchuk", 4, 2018, "Best if you want to create content")
              ]


@app.get("/Books/")
async def get_books():
    return Book_store

@app.get("/Books")
async def get_books(book_id: int):
    for book in Book_store:
        if book.id == book_id:
            return book
        
@app.get("/Books/{book_rating}")
async def get_book_by_rating(book_rating: int):
    books_to_return = []
    for book in Book_store:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return

@app.post("/create_book")
async def create_books(book: book_request):
    new_book = Book(**book.model_dump())
    print(type(new_book))
    Book_store.append(find_book_id(new_book))


def find_book_id(book: Book):
    if len(Book_store) > 0:
        book.id = Book_store[-1] + 1

    else:
        book.id = 1

    return book

@app.delete("/Books/{book_id}")
async def delete_book_by_id(book_id: int ):
    for i in range(len(Book_store)):
        if Book_store[i].id == book_id:
            Book_store.pop(i)
            return



