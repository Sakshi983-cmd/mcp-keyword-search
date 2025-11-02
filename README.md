🚀 MCP Keyword Search Tool
🧩 Overview
This FastAPI-based MCP server lets users upload .txt or .pdf files and search for any keyword inside them. Built for Ressel AI Assignment – Task 2 (MCP Server Development).

⚙️ Features
📁 Upload .txt or .pdf files

🔍 Search for any keyword

📊 Get total keyword occurrences in JSON

⚡ Built with FastAPI + Uvicorn

🧱 Project Structure
Code
mcp-keyword-search/
├── src/
│   └── mcp_keyword_search/
│       ├── __init__.py
│       └── server.py
├── requirements.txt
├── pyproject.toml
├── README.md
└── sample.txt
🧰 Tech Stack
Component	Description
Language	Python 3.10+
Framework	FastAPI
Server	Uvicorn
IDE	VS Code
▶️ Run Locally
1. Clone the Repo
bash
git clone https://github.com/<your-username>/mcp-keyword-search.git
cd mcp-keyword-search
2. Install Dependencies
bash
pip install -r requirements.txt
3. Start the Server
bash
python src/mcp_keyword_search/server.py
📮 API Usage
🔹 Endpoint
http
POST /search
🔹 Form Data
Field	Value
keyword	"AI"
file	sample.txt
🔹 Sample Response
json
{
  "keyword": "AI",
  "occurrences": 4
}
