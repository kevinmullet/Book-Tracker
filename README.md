# Book Tracker API

A simple RESTful API built with **FastAPI**, **SQLAlchemy**, and **SQLite** to manage a personal book collection.

This project demonstrates fundamental backend development concepts, including CRUD operations, database integration, request validation, and REST API design.

## Tech Stack

- **Python** — Programming language
- **FastAPI** — Web framework for building REST APIs
- **SQLAlchemy** — ORM for database operations
- **SQLite** — Relational database
- **Pydantic** — Data validation

## Features

- Add new books
- Retrieve all books
- Retrieve a book by ID
- Update book information
- Delete books
- Handle invalid requests and missing records

Each book contains:
- `id` — Unique identifier
- `title` — Book title
- `author` — Book author
- `status` — Reading status (default: `want_to_read`)

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API home |
| POST | `/books` | Add a new book |
| GET | `/books` | Retrieve all books |
| GET | `/books/{book_id}` | Retrieve a book by ID |
| PUT | `/books/{book_id}` | Update a book |
| DELETE | `/books/{book_id}` | Delete a book |

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/USERNAME/book-tracker-api.git
cd book-tracker-api
```

Replace `USERNAME` with your GitHub username.

**2. Create a virtual environment**

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

**3. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

**4. Run the application**

```bash
python -m uvicorn app.main:app --reload
```

**5. Open API documentation**

Visit:

http://127.0.0.1:8000/docs

FastAPI automatically generates interactive API documentation using Swagger UI.

## Example Request

**POST `/books`**

```json
{
  "title": "Atomic Habits",
  "author": "James Clear",
  "status": "want_to_read"
}
```

**Example Response**

```json
{
  "id": 1,
  "title": "Atomic Habits",
  "author": "James Clear",
  "status": "want_to_read"
}
```

## Project Structure

```text
book-tracker-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── schemas.py
├── .gitignore
├── requirements.txt
└── README.md
```

## What I Learned

Through this project, I practiced:

- Building RESTful APIs with FastAPI
- Implementing CRUD operations
- Connecting Python applications to SQLite using SQLAlchemy
- Validating request data with Pydantic
- Managing database sessions using dependency injection
- Handling HTTP errors and testing endpoints using Swagger UI
- Managing source code with Git and GitHub

## Future Improvements

- Add authentication and user accounts
- Implement filtering by reading status
- Add automated API tests using pytest
- Add pagination for large book collections
