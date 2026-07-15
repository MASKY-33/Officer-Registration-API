import json

from fastapi import FastAPI

from pydantic import BaseModel


app = FastAPI()






class Officer(BaseModel):
    name: str
    badge_id: int
    is_active: bool

@app.post("/add-officer")

def create_officer(officer: Officer):
    return officer
