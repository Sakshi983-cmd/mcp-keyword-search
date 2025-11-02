markdown
# 🚀 MCP Keyword Search Tool

## 🧩 Overview
This FastAPI-based MCP server allows users to upload `.txt` or `.pdf` files and search for any keyword inside them.  
Built as part of the **Ressel AI Assignment – Task 2 (MCP Server Development)**.

---

## ⚙️ Features
- 📁 Upload `.txt` or `.pdf` files  
- 🔍 Search for any keyword  
- 📊 Get total keyword occurrences in JSON format  
- ⚡ Built using **FastAPI**, **Python**, and **Uvicorn**

## 🧰 Tech Stack

| Component   | Description         |
|------------|---------------------|
| Language    | Python 3.10+        |
| Framework   | FastAPI             |
| Server      | Uvicorn             |
| IDE         | VS Code             |

---

## ▶️ How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/mcp-keyword-search.git
cd mcp-keyword-search
2. Install Dependencies
bash
pip install -r requirements.txt
3. Run the Server
bash
python src/mcp_keyword_search/server.py
📮 API Usage
🔹 Endpoint
http
POST /search
🔹 Form Data
Field	Type	Example
keyword	string	"AI"
file	file	sample.txt
🔹 Sample Response
json
{
  "keyword": "AI",
  "occurrences": 4
}
🖼️ Swagger UI Screenshot
✅ Successful run via FastAPI Swagger interface (Insert screenshot here)

💡 Learning Outcomes
✅ Built a modular FastAPI server

✅ Implemented keyword search logic for .txt and .pdf

✅ Learned file handling, routing, and JSON response formatting

✅ Practiced clean code and scalable backend design

🙌 Author
Sakshi Tiwari AI/ML Engineer | Ethical AI Enthusiast | Builder of Privacy-First Solutions 

