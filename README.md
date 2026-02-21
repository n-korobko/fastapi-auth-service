# FastAPI Auth Service

## Project Description

This project is a backend authentication service built with **FastAPI**.
It provides:

* User registration
* User authentication (JWT)
* PostgreSQL database integration
* Alembic migrations
* PDF profile generation
* Full Docker support

The project uses asynchronous SQLAlchemy with PostgreSQL.

---

# Tech Stack

* Python 3.11
* FastAPI
* SQLAlchemy (async)
* PostgreSQL 15
* Alembic
* JWT (python-jose)
* Passlib (password hashing)
* ReportLab (PDF generation)
* Docker & Docker Compose

---

# Project Structure

```
fastapi-auth-service/
│
├── app/
│   ├── core/          # security, config
│   ├── db/            # database connection
│   ├── models/        # SQLAlchemy models
│   ├── routers/       # API routes
│   ├── schemas/       # Pydantic schemas
│   ├── services/      # business logic + PDF service
│   └── main.py        # FastAPI entry point
│
├── alembic/           # database migrations
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── alembic.ini
```

---

# Environment Variables

Database connection is configured for Docker:

```
postgresql+asyncpg://user:password@db:5432/fastapi_db
```

If needed, you can move this into a `.env` file.

---

# How to Run the Project

## 1️⃣ Prerequisites

Make sure you have installed:

* Docker
* Docker Compose

---

## 2️⃣ Build and Start Containers

From the project root directory:

```
docker compose up --build
```

After the first build, you can start with:

```
docker compose up
```

To run in background:

```
docker compose up -d
```

To stop containers:

```
docker compose down
```

---

# Database Migrations (Alembic)

Create a new migration:

```
docker compose exec app alembic revision --autogenerate -m "message"
```

Apply migrations:

```
docker compose exec app alembic upgrade head
```

---

# API Documentation

After the containers are running, open:

```
http://localhost:8000/docs
```

Swagger UI will be available.

---

# Authentication Flow

1. Register user
2. Login with email & password
3. Receive JWT token
4. Use token in Authorization header:

```
Authorization: Bearer <your_token>
```

---

# PDF Generation

Authenticated users can generate a PDF profile.
The PDF contains:

* User ID
* Name
* Surname
* Email
* Date of birth

The file is returned as a downloadable PDF response.

---

# Features Implemented

* Async database connection
* Password hashing
* JWT authentication
* Protected routes
* Alembic migrations
* Dockerized environment
* PostgreSQL volume persistence
* PDF generation service

---

# Notes

* Tables are managed only through Alembic migrations.
* The database runs inside Docker.
* Data is persisted using Docker volumes.

---

# API Request Examples

## 🔹 Register User

```bash
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Anna",
    "surname": "Smith",
    "email": "anna@example.com",
    "date_of_birth": "2000-01-01",
    "password": "password123"
  }'
```

---

## 🔹 Login

```bash
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "anna@example.com",
    "password": "password123"
  }'
```

Response example:

```json
{
  "access_token": "your_jwt_token",
  "token_type": "bearer"
}
```

---

## 🔹 Get Protected Profile (with JWT)

```bash
curl -X GET http://localhost:8000/auth/me \
  -H "Authorization: Bearer your_jwt_token"
```

---

## 🔹 Generate PDF Profile

```bash
curl -X GET http://localhost:8000/auth/me/pdf \
  -H "Authorization: Bearer your_jwt_token" \
  --output profile.pdf
```

---


FastAPI Authentication Service

