# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI is running"}

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks once on startup
with open("marks.json", "r") as f:
    marks_data = json.load(f)

@app.get("/api")
def get_marks(name: list[str] = []):
    result = [marks_data.get(n, None) for n in name]
    return {"marks": result}
