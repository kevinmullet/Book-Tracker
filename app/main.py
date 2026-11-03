from fastapi import FastAPI, Depends, HTTPException
from app.database import Base,engine, get_db
from app.models import Book 
from sqlalchemy.orm import Session
from app.schemas import BookCreate

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
def home():
    return {"message":"Book tracker main menu"}

@app.post('/books')
def create_book(book:BookCreate, db:Session = Depends(get_db)):
    new_book = Book(title=book.title, author=book.author, status=book.status)

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book

@app.get('/books')
def get_books(db: Session = Depends(get_db)):
    Books = db.query(Book).all()
    return Books

@app.get('/books/{book_id}')
def get_book(book_id = int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    
    if book == None:
        raise HTTPException(status_code=404,detail='book not found')
    return book

@app.delete('/books/{book_id}')
def delete_book(book_id = int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()

    if book == None:
        raise HTTPException(status_code=404,detail='book not found')

    db.delete(book)
    db.commit()

    return {"message": "Book deleted successfully"}

@app.put('/books/{book_id}')
def update_book(book_id:int, updated_data: BookCreate,db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()

    if book == None:
        raise HTTPException(status_code='404',detail='book not found')

    book.title = updated_data.title
    book.status = updated_data.status
    book.author = updated_data.author

    db.commit()
    db.refresh(book)

    return book
