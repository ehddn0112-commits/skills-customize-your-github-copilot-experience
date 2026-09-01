# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API with FastAPI that lets users manage a small collection of books. You will define routes, use Pydantic models to validate data, and return appropriate HTTP responses.

## 📝 Tasks

### 🛠️	Create Your FastAPI Application

#### Description

Set up the FastAPI application and create routes that allow users to view book data.

#### Requirements

Completed program should:

- Create a FastAPI application in `starter-code.py`.
- Store at least three books in an in-memory list.
- Provide a `GET /books` route that returns every book.
- Provide a `GET /books/{book_id}` route that returns one matching book.
- Return a 404 response when the requested book does not exist.


### 🛠️	Add Validated Book Data

#### Description

Define a Pydantic model and use it to validate book information sent to your API.

#### Requirements

Completed program should:

- Define a `Book` model with `id`, `title`, and `author` fields.
- Use the `Book` model as the response model for book routes.
- Add a `POST /books` route that accepts a new book.
- Add the new book to the in-memory list and return it with status code 201.


### 🛠️	Update and Delete Books

#### Description

Complete the REST API by allowing users to edit and remove existing books.

#### Requirements

Completed program should:

- Add a `PUT /books/{book_id}` route that updates a matching book.
- Add a `DELETE /books/{book_id}` route that removes a matching book.
- Return a 404 response for update or delete requests with an unknown ID.
- Test every route using the interactive documentation at `/docs`.
