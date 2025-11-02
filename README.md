***# 🚀 MCP Keyword Search Tool

## 🧩 Overview
This project implements a **Model-Context Protocol (MCP) server** using **FastAPI**.  
The tool allows users to upload a text or PDF file and search for a specific keyword inside it.  
It was built as part of the **Ressel AI Assignment – Task 2 (MCP Server Development)**.

---

## ⚙️ Features
✅ Upload `.txt` or `.pdf` files  
✅ Enter any keyword to search within the file  
✅ Returns total keyword occurrences in JSON format  
✅ Built using **FastAPI**, **Python**, and **Uvicorn**

---

## 🧱 Project Structure
mcp-keyword-search/
├── src/
│ └── mcp_keyword_search/
│ ├── init.py
│ └── server.py
├── requirements.txt
├── pyproject.toml
├── README.md
└── sample.txt

yaml
Copy code

---

## 🧰 Tech Stack
- **Language:** Python 3.10 +  
- **Framework:** FastAPI  
- **Server:** Uvicorn  
- **IDE:** VS Code  

---

## ▶️ How to Run Locally
1. **Clone this repository**
   ```bash
   git clone https://github.com/<your-username>/mcp-keyword-search.git
   cd mcp-keyword-search
Install dependencies

bash
Copy code
pip install -r requirements.txt
Run the server

bash
Copy code
python src/mcp_keyword_search/server.py
Open your browser

Visit 👉 http://127.0.0.1:8000/docs

Upload a file and enter a keyword (e.g., "AI")

Click Execute

📊 Sample Output
Request Example

bash
Copy code
POST /search
keyword = "AI"
file = sample.txt
Response

json
Copy code
{
  "keyword": "AI",
  "occurrences": 4
}
🧩 Screenshot
Below is the successful execution proof from the FastAPI interface 👇


💡 Learning Outcomes
Built and deployed an API using FastAPI

Learned handling file uploads and multipart form data

Implemented keyword search using Python I/O operations

