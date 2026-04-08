from fastapi import FastAPI
 
from fastapi import Request
from fastapi.templating import Jinja2Templates

app =FastAPI()
templates = Jinja2Templates (directory="templates")
posts: list[dict] = [
    {"id": 1, "title": "First Post", "content": "This is the first post."},
    {"id": 2, "title": "Second Post", "content": "This is the second post."},
    {"id": 3, "title": "Third Post", "content": "This is the third post."},
]
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse( request=request,
        name="home.html" , context={"posts":posts,"title":"Awesome application!"}
        
    )
 
@app.get("/nice")
def nicerhome():
    return "<h1>Fast api is awesome</h1>"

@app.get("/api/posts")
def getposts():
    return posts