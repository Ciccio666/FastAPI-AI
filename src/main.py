from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import uvicorn

from . import crud, models, schemas
from .database import engine, get_db
from .config import settings

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.API_TITLE,
    version=settings.API_VERSION,
)

@app.get("/")
async def root():
    """
    Root endpoint that returns basic API information.
    """
    return {
        "title": settings.API_TITLE,
        "version": settings.API_VERSION,
        "message": "Welcome to the FastAPI application",
        "endpoints": {
            "items": "/items/",
            "docs": "/docs",
            "openapi": "/openapi.json"
        }
    }

@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve all items with pagination support.
    """
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@app.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific item by ID.
    """
    return crud.get_item(db, item_id)

@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    """
    Create a new item.
    """
    return crud.create_item(db, item)

@app.put("/items/{item_id}", response_model=schemas.Item)
def update_item(item_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    """
    Update an existing item.
    """
    return crud.update_item(db, item_id, item)

@app.delete("/items/{item_id}", response_model=schemas.Item)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """
    Delete an item.
    """
    return crud.delete_item(db, item_id)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)