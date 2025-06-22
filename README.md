# 📝 NotesApp with MCP Server and LangGraph Agent

A simple yet powerful note-taking application demonstrating modern AI tool integration using **FastAPI**, **LangGraph**, and **MCP (Multimodal Communication Protocol)**.

---

## 🧠 Features

- 🔐 User Registration & Login
- 🗒️ Add, Retrieve, and Delete Notes
- 🔧 MCP Tool Interface for Notes Management
- 🤖 LangGraph Agent using OpenAI + MCP Toolset

---

## 📦 Project Structure

```
.
├── main.py         # MCP tool server entry point
├── app.py          # FastAPI backend for notes API
├── agent.py        # LangGraph agent logic
└── README.md       # Documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/NotesApp-MCP.git
cd NotesApp-MCP
```

### 2. Install Dependencies

```bash
uv add fastapi uvicorn pymongo langgraph openai "mcp[cli]" langchain langchain_mcp_adapters
```

🔗 [Install uv](https://docs.astral.sh/uv/getting-started/installation/)

### 3. Start FastAPI Backend

```bash
uvicorn app:app --reload
```

### 4. Start MCP Tool Server

```bash
uv run main.py
# For developer web version:
uv run mcp dev main.py
```

### 5. Run LangGraph Agent

```bash
uv run agent.py
```

---

## 🔐 Environment Variables

Set your OpenAI key before starting the agent (e.g., in `agent.py`):

```python
os.environ["OPENAI_API_KEY"] = "sk-..."
```

---

## 🧰 Available MCP Tools

| Function                | Description                        |
|-------------------------|------------------------------------|
| `add_note_for_user()`   | Adds a new note                    |
| `get_notes_for_user()`  | Retrieves all notes for a user     |
| `get_note_by_id()`      | Gets a specific note by its ID     |
| `delete_note_by_id()`   | Deletes a specific note by its ID  |

---

## 💬 Sample Prompt

```text
Query: Add a note saying "Meeting at 10am" for user ID 123456
Response: Note added successfully. Note ID: 23435435
```

---

## 📄 License

This project is licensed under the [MIT LICENSE](./LICENSE.md).