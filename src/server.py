from fastapi import FastAPI, UploadFile, Form
import uvicorn

app = FastAPI(title="MCP Keyword Search Tool")

@app.post("/search")
async def search_keyword(keyword: str = Form(...), file: UploadFile = None):
    if not file:
        return {"error": "No file uploaded"}
    content = await file.read()
    text = content.decode("utf-8")
    count = text.lower().count(keyword.lower())
    return {"keyword": keyword, "occurrences": count}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
