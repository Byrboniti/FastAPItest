from fastapi import FastAPI
from schemas import Book, Author, BookOut
from fastapi import Query, Body
from typing import List
# uvicorn main:app


app = FastAPI()


# @app.get('/')
# def home():
#     return {'key': ' hello'}

# @app.get("/{pk}")
# def get_item(pk:int,q: str= None):
#     return {'key':pk, 'q': q}
#
# @app.get('/user/{pk}/items/{item}/')
# def get_user_item(pk:int, item:str):
#     return {"user": pk,"item":item}

# @app.post('/book')
# def create_book(item: Book, author: Author, quantity: int = Body(...)):
#     return {'item': item, 'author' : author, 'quantity': quantity}
@app.post('/book',response_model=BookOut,)
async def create_book(item: Book):
    print(item.dict())
    return BookOut(**item.dict(), id=3)

@app.get('/book')
def get_book(q: List[str] = Query("test",  description="description",)):
    return q

@app.get('/book/{pk}')
def get_single_book(pk: int):
    return {'pk': pk}

@app.post('/author')
def create_author(author: Author = Body(..., embed=True)):
    return {'author': author}