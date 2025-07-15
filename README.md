<!-- TOC -->
* [FastAPI PostgreSQL CRUD Example](#fastapi-postgresql-crud-example)
  * [Prerequisites](#prerequisites)
  * [Project Structure](#project-structure)
  * [Usage](#usage)
    * [1. Configure your database](#1-configure-your-database)
    * [2. Install dependencies](#2-install-dependencies)
    * [3. Run the application](#3-run-the-application)
    * [4. Explore the API](#4-explore-the-api)
    * [5. Example Requests](#5-example-requests)
      * [Create a user](#create-a-user)
      * [List all users](#list-all-users)
      * [Get a single user](#get-a-single-user)
      * [Update a user](#update-a-user)
      * [Delete a user](#delete-a-user)
<!-- TOC -->

# FastAPI PostgreSQL CRUD Example

A minimal CRUD application using FastAPI, SQLAlchemy and PostgreSQL, with absolute imports and a clear project structure.

## Prerequisites

- **Python 3.7+**  
- **PostgreSQL** installed and running
- `psql` command‑line tool (or any other Postgres client)

## Project Structure
- **app/main.py**: Application entrypoint.
- **app/api/routers.py**: API routes.
- **app/schemas/user_schema.py**: Pydantic schemas.
- **app/models/user.py**: SQLAlchemy ORM models.
- **app/repositories/user_repository.py**: Database operations.
- **app/services/user_service.py**: Business logic.
- **app/db/session.py**: Database session and connection.
- **app/db/base.py**: Declarative base.

```
.
├── .env
├── README.md
├── requirements.txt
└── app
    ├── __init__.py
    ├── main.py
    ├── api
    │   ├── __init__.py
    │   └── routers.py
    ├── db
    │   ├── __init__.py
    │   ├── base.py
    │   └── session.py
    ├── models
    │   ├── __init__.py
    │   └── user.py
    ├── repositories
    │   ├── __init__.py
    │   └── user_repository.py
    ├── schemas
    │   ├── __init__.py
    │   └── user_schema.py
    └── services
        ├── __init__.py
        └── user_service.py
```

## Usage

### 1. Configure your database

1. Open `.env` (in project root) and set your `DATABASE_URL`, for example:
   ```dotenv
   DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/mydatabase
   ```
2. Create the database in PostgreSQL:
   ```bash
   psql -U postgres
   CREATE DATABASE mydatabase;
   \q
   ```

### 2. Install dependencies

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate        # macOS/Linux
   # venv\Scripts\activate.bat   # Windows
   ```
2. Upgrade `pip` and install:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

### 3. Run the application

From the project root (where `app/` folder lives):

```bash
uvicorn app.main:app --reload
```

- **Host:** `127.0.0.1`  
- **Port:** `8000`

> **Alternative**: if you ever switch to absolute imports without the top‑level `app` package in your `PYTHONPATH`, you can run:
> ```bash
> uvicorn main:app --reload --app-dir app
> ```

### 4. Explore the API

FastAPI automatically generates interactive docs:

- **Swagger UI**:  http://127.0.0.1:8000/docs  
- **ReDoc**:       http://127.0.0.1:8000/redoc

Here you can perform all CRUD operations on the `/users` endpoint.

### 5. Example Requests

#### Create a user

```bash
curl -X POST "http://127.0.0.1:8000/users/"      -H "Content-Type: application/json"      -d '{"name":"Alice","email":"alice@example.com"}'
```

#### List all users

```bash
curl http://127.0.0.1:8000/users/
```

#### Get a single user

```bash
curl http://127.0.0.1:8000/users/1
```

#### Update a user

```bash
curl -X PUT "http://127.0.0.1:8000/users/1"      -H "Content-Type: application/json"      -d '{"name":"Alice Smith","email":"alice.smith@example.com"}'
```

#### Delete a user

```bash
curl -X DELETE http://127.0.0.1:8000/users/1
```

> **Tip**: You can also use HTTPie for nicer syntax:
> ```bash
> http POST http://127.0.0.1:8000/users/ name="Alice" email="alice@example.com"
> http GET   http://127.0.0.1:8000/users/
> http PUT   http://127.0.0.1:8000/users/1 name="Alice Smith" email="alice.smith@example.com"
> http DELETE http://127.0.0.1:8000/users/1
> ```
