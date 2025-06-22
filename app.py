from fastapi import FastAPI
from pymongo import MongoClient
import os
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this in production: ["https://yourdomain.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

mongo_uri = os.getenv('MONGO_URI', 'your_mongo_uri_here')  # Replace with your MongoDB URI
client = MongoClient(mongo_uri)
db = client['mcp-test']  
users = db['users']
notes = db['notes']

@app.get("/")
async def root():
    return {"message": "API is running"}

@app.post("/register")
async def register_user(username: str, password: str):
    if users.find_one({"username": username}):
        return {"message": "User already exists"}
    users.insert_one({"username": username, "password": password})
    return {"message": "User registered successfully"}

@app.post("/login")
async def login_user(username: str, password: str):
    user = users.find_one({"username": username, "password": password})
    
    # Return user id if login is successful
    if user:
        return {"message": "Login successful", "user_id": str(user["_id"])}
    else:
        return {"message": "Invalid username or password"}
    
class Note(BaseModel):
    user_id: str
    note: str

@app.post("/add_note")
async def add_note(note: Note):
    user_id = note.user_id
    note = note.note
    notes.insert_one({"user_id": user_id, "note": note})
    
    # Return success message and note id
    note_id = str(notes.find_one({"user_id": user_id, "note": note})["_id"])
    return {"message": "Note added successfully", "note_id": note_id}

@app.get("/get_notes/{user_id}")
async def get_notes(user_id: str):
    user_notes = notes.find({"user_id": user_id})
    
    # Return list of notes for the user
    return {"notes": [{"note_id": str(note["_id"]), "note": note["note"]} for note in user_notes]}

@app.get("/get_note/{note_id}")
async def get_note(note_id: str):
    note_object_id = ObjectId(note_id)
    note = notes.find_one({"_id": note_object_id})
    
    # Return note details if found
    if note:
        return {"note_id": str(note["_id"]), "note": note["note"]}
    else:
        return {"message": "Note not found"}
    

@app.delete("/delete_note/{note_id}")
async def delete_note(note_id: str):
    note_object_id = ObjectId(note_id)
    result = notes.delete_one({"_id": note_object_id})
    
    # Return success message if note was deleted
    if result.deleted_count > 0:
        return {"message": "Note deleted successfully"}
    else:
        return {"message": "Note not found"}




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.1", port=8000)