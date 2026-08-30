import os
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI
from supabase import create_client, Client

# Load .env file explicitly from current directory
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise ValueError("SUPABASE_URL or SUPABASE_KEY is missing from .env file!")

# Initialize Supabase client
supabase: Client = create_client(url, key)

# Initialize FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Server and Supabase client configured successfully!"}