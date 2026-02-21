from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Book:
    id: int
    title: str 
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class Bookrequest(BaseModel):
    id: Optional[int] = Field(description="ID is not needed in create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)

    model_config = {
        "json_schema_extra": {
            "example":{
                "title" : "A new Book",
                "author": "codingwithfarhan",
                "description": "A new description of a book",
                "rating": 5
            }
        }
    }
    

BOOKS = [Book(1, "Computer Science Pro", "codingwithfarhan", "A very nice Book", 5),
         Book(2, "Be Fast With FastAPI", "codingwithfarhan", "This is a great book",5),
         Book(3, "Master endpoints","codingwithfarhan", "A awesome book", 5),
         Book(4, "HP1", "Author 1", "Book Description", 2),
         Book(5, "HP2", "Author 2", "Book Description", 3),
         Book(6, "HP3", "Author 3", "Book Description", 1)]

@app.get("/books")
async def get_books():
    return BOOKS

@app.post("/books")
async def create_books(book_request: Bookrequest):
    # print(type(book_request))
    new_book = Book(**book_request.model_dump())
    print(type(new_book))
    BOOKS.append(find_book_id(new_book))

def find_book_id(book: Book):

    # book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1

    return book