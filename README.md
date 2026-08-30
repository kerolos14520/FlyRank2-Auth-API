# FlyRank FastAPI & Supabase Auth API

A production-ready Authentication API built with **FastAPI** and **Supabase Auth**, featuring endpoints for user registration, authentication, protected user profile retrieval, and session termination.

---

## Features

- **User Signup (`POST /auth/signup`)**: Registers new users in Supabase Auth.
- **User Login (`POST /auth/login`)**: Authenticates credentials and returns a Bearer JWT access token.
- **Get User Profile (`GET /auth/me`)**: Protected route that verifies JWT tokens and retrieves current user details.
- **User Logout (`POST /auth/logout`)**: Terminates active user sessions in Supabase.

---

## Tech Stack

- **Framework**: FastAPI
- **Database & Auth**: Supabase
- **Data Validation**: Pydantic v2 (with `email-validator`)
- **Server**: Uvicorn
- **Environment Management**: `python-dotenv`

---

## Project Setup

### 1. Clone the Repository

```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
cd FlyRank2