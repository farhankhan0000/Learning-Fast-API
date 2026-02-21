from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Book:
    id : int
    name : int
    author: int
    rating: int
    review: int

    def __init__(self, id, name, author, rating, review):
        self.id = id
        self.name = name
        self.author = author
        self.rating = rating
        self.review = review

class Bookrequest(BaseModel):
    id: Optional[int] = Field(description="ID is not needed on create", default=None)
    name: str = Field(min_length=3)
    author: str = Field(min_length=2)
    rating: int = Field(gt=1, lt=6)
    review: str = Field(min_length=1, max_length=100)


    model_config  = {
        "json_schema_extra": {
            "example": {
                
            }
        }
    }

    

BOOKS = [Book(1, "Metamorphosis", "Franz Kafka", 9, "Book that showed fragility of Human Identity"),
         Book(2, "The Trial", "Franz Kafka", 8, "It was an awesome book"),
         Book(3, "12 Rules For Life", "Jordan B Peterson", 10, "This Book is an antitode to chaos"),
         Book(4, "Think and grow rich", "Napolean Hill", 8, "Clear the mindset and thinking about money")]


@app.get("/books")
async def get_books():
    return BOOKS

@app.post("/books")
async def create_books(book_request: Bookrequest):
    new_book = Book(**book_request.model_dump())
    print(type(new_book))
    BOOKS.append(new_book)

def find_id(book: Book):

    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1

    return book