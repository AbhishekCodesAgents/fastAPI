from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


## swagger url is : http://localhost:8000/docs

@app.get("/allBooks")
async def get_all_books():
    return BOOKS




@app.get("/allBooks/title/{book_title}")
async def first_api(book_title:str):
    for book in BOOKS:
        if(book.get('title').casefold() == book_title.casefold()):
            return book
        else:
            return {"message" : "no books available for title {book_title}"}

## http://127.0.0.1:8000/allBooks/?category=SCIENCE
@app.get("/allBooks/")
async def category_book_query_param(category:str):
    books_to_return = []

    for book in BOOKS:
        if(book.get('category').casefold() == category.casefold()):
            books_to_return.append(book)
        else:
            pass

    return books_to_return

## http://127.0.0.1:8000/allBooks/Author%20one/?category=science
@app.get("/allBooks/{author}/")
async def get_books_author_by_category(author:str, category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold() and book.get('category'.casefold()) == category.casefold():
            books_to_return.append(book)
        else:
            pass
    return books_to_return