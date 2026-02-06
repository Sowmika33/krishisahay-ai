from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from backend.vector_store import search

app = FastAPI()
templates = Jinja2Templates(directory="backend/templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask_ai(query: Query):
    try:
        result = search(query.question)
        return {
            "question": query.question,
            "answer": result
        }
    except Exception as e:
        return {"error": str(e)}
