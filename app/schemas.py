from pydantic import BaseModel


class BookCreate(BaseModel):
    title: str
    author: str
    status: str = "want_to_read" # default value