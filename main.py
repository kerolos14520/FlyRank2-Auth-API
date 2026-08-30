import os
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, EmailStr
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
app = FastAPI(title="FlyRank Auth API")

# Security Scheme for Swagger UI
security = HTTPBearer()

# Schemas
class UserSignUp(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Helper Dependency: Authenticate Requests
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        # Retrieve user details from Supabase using the access token
        user_response = supabase.auth.get_user(token)
        if not user_response.user:
            raise HTTPException(status_code=401, detail="Invalid token or expired session")
        return user_response.user
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Authentication failed: {str(e)}")

# Routes
@app.get("/")
def read_root():
    return {"message": "Server and Supabase client configured successfully!"}

@app.post("/auth/signup")
def sign_up(user_data: UserSignUp):
    try:
        response = supabase.auth.sign_up({
            "email": user_data.email,
            "password": user_data.password,
        })
        return {
            "message": "User created successfully",
            "user": response.user
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/auth/login")
def login(credentials: UserLogin):
    try:
        response = supabase.auth.sign_in_with_password({
            "email": credentials.email,
            "password": credentials.password,
        })
        return {
            "message": "Login successful",
            "access_token": response.session.access_token,
            "token_type": "bearer",
            "user": response.user
        }
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid email or password")

@app.get("/auth/me")
def get_user_profile(current_user = Depends(get_current_user)):
    return {
        "message": "Protected route accessed successfully",
        "user": current_user
    }