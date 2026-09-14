from database import Base,engine, get_db
from models import Note
from fastapi import FastAPI,Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import NoteCreate, NoteResponse
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174","http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

@app.post("/api/notes/add", response_model=NoteResponse)
def add_note(response: NoteCreate, db:Session=Depends(get_db)):
    note=Note(title=response.title, content=response.content)
    db.add(note)
    db.commit()
    db.refresh(note)
    message=NoteResponse(id=note.id,title=note.title,content=note.content)
    return message

@app.get("/api/notes/", response_model=list[NoteResponse])
def get_all(db:Session=Depends(get_db)):
    notes=db.query(Note).all()
    return notes

@app.get("/api/notes/{id}", response_model=NoteResponse)
def get_each(id:int, db:Session=Depends(get_db)):
    note=db.query(Note).filter(Note.id==id).first()

    if note is None:
        raise HTTPException(status_code=404, detail="Note does not exist")
    return note

@app.put("/api/notes/{id}", response_model=NoteResponse)
def update_note(id:int, note:NoteCreate, db:Session=Depends(get_db)):
    note_db=db.query(Note).filter(Note.id==id).first()
    if note_db is None:
        raise HTTPException(status_code=404,detail="Note does not exist")
    note_db.title=note.title
    note_db.content=note.content

    db.commit()
    db.refresh(note_db)
    return note_db

@app.delete("/api/notes/{id}")
def delete_note(id:int, db:Session=Depends(get_db)):
    note=db.query(Note).filter(Note.id==id).first()
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)
    db.commit()

    return {"message": f" note with {id} has been deleted successfully"}