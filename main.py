from mcp.server.fastmcp import FastMCP
import requests
from typing import List
import json

mcp = FastMCP("NotesApp")


@mcp.tool(name="add_note_for_user", description="Adds a note for a specific user.")
async def add_note_for_user(data:List[dict]) -> dict:
    """
    Adds a note for a specific user.

    Args:
       {
        "user_id": str,
        "note": str
        }

    Returns:
        dict: A message indicating the result of adding the note, including the note ID.
    """

    payload = data[0]
    response = requests.post("http://localhost:8000/add_note", headers={"Content-Type": "application/json", "Accept": "application/json"}, data=json.dumps(payload))
    
    return response.json()
    


@mcp.tool(name="get_notes_for_user", description="Retrieves all notes for a specific user.")
async def get_notes_for_user(user_id: str) -> dict:
    """
    Retrieves all notes for a specific user.

    Args:
        user_id (str): The ID of the user.

    Returns:
        dict: A list of notes for the user.
    """
    response = requests.get(f"http://localhost:8000/get_notes/{user_id}", headers={"Content-Type": "application/json", "Accept": "application/json"})
    
    return response.json()

@mcp.tool(name="get_note_by_id", description="Retrieves a note by its ID.")
async def get_note_by_id(note_id: str) -> dict:
    """
    Retrieves a note by its ID.

    Args:
        note_id (str): The ID of the note.

    Returns:
        dict: The note details if found, otherwise an error message.
    """
    response = requests.get(f"http://localhost:8000/get_note/{note_id}", headers={"Content-Type": "application/json", "Accept": "application/json"})
    
    return response.json()

@mcp.tool(name="delete_note_by_id", description="Deletes a note by its ID.")
async def delete_note_by_id(note_id: str) -> dict:
    """
    Deletes a note by its ID.

    Args:
        note_id (str): The ID of the note.

    Returns:
        dict: A message indicating the result of the deletion.
    """
    response = requests.delete(f"http://localhost:8000/delete_note/{note_id}", headers={"Content-Type": "application/json", "Accept": "application/json"})
    
    return response.json()


if __name__ == "__main__":
    mcp.run(transport="stdio")