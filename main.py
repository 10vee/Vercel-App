from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "FastAPI is running"}

@app.get("/api")
def get_marks(name: list[str] = []):
    try:
        with open("marks.json", "r") as f:
            marks_data = json.load(f)
    except Exception as e:
        return {"error": f"Could not load marks.json: {str(e)}"}
    
    result = [marks_data.get(n, None) for n in name]
    return {"marks": result}
