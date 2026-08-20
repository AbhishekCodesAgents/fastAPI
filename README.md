# fastAPI

# create a virtual environment
uv venv fastapienv

# activate the environment
fastapienv\Scripts\activate

# install fastapi
uv pip install fastapi

# webserver for fastapi is uvicorn
uv pip install uvicorn

# Your path to add in PyCharm will simply be:C:\Users\Abhishek\PycharmProjects\fastAPI\.venv\Scripts\python.exe
uv init

# run the application
uvicorn src.fastapi.books:app --reload or uvicorn --app-dir .. src.fastapi.books:app --reload

