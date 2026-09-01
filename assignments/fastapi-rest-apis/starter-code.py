from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    author: str


books = [
    Book(id=1, title="The Hobbit", author="J. R. R. Tolkien"),
    Book(id=2, title="A Wrinkle in Time", author="Madeleine L'Engle"),
    Book(id=3, title="The Giver", author="Lois Lowry"),
]


@app.get("/books", response_model=list[Book])
def get_books():
    # TODO: Return every book in the list.
    pass


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    # TODO: Return the matching book or raise HTTPException(status_code=404).
    pass


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: Book):
    # TODO: Add the new book to the list and return it.
    pass


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    # TODO: Replace the matching book or raise HTTPException(status_code=404).
    pass


@app.delete("/books/{book_id}", response_model=Book)
def delete_book(book_id: int):
    # TODO: Remove and return the matching book or raise HTTPException(status_code=404).
    pass


# Run the API with: uvicorn starter-code:app --reload
