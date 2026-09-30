# Employee Management API

A FastAPI-based employee management system for creating, retrieving, updating, and deleting employee records. The application uses PostgreSQL as the database, SQLAlchemy for ORM support, and Pydantic for request validation and response models.

## Overview

This project demonstrates a clean backend architecture for a simple CRUD application. It is designed to manage employee data such as name, email, department, and salary while enforcing validation rules and handling database constraints such as unique email addresses.

## Tech Stack

- Python 3.10+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Uvicorn
- Pytest
- Swagger / OpenAPI

## Features

- Create new employee records
- Retrieve all employees
- Fetch a single employee by ID
- Update employee information
- Delete employee records
- Validate required fields and data types
- Enforce positive salary values
- Ensure email format is valid
- Prevent duplicate email entries using database constraints
- Generate interactive API docs automatically via Swagger UI
- Include automated tests for app behavior

## Project Structure

```text
Employee Management API/
├── app/
│   ├── __init__.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── routers/
│       ├── __init__.py
│       └── employees.py
├── tests/
│   ├── __init__.py
│   └── test_employees.py
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── venv/
```

## Prerequisites

Before running the project, make sure you have:

- Python installed
- PostgreSQL installed and running
- A PostgreSQL database created for the app
- A virtual environment tool such as `venv`

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd "Employee Management API"
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Environment Setup

Create a `.env` file in the project root and add your database URL:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/employee_db
```

Replace the values with your actual PostgreSQL credentials and database name.

## Running the Application

Start the FastAPI server with Uvicorn:

```bash
uvicorn app.main:app --reload
```

The application will start at:

- http://127.0.0.1:8000
- Swagger docs: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## API Endpoints

### Root

- GET `/`  
  Returns a simple health/status response.

### Employees

- POST `/employees/`  
  Create a new employee

- GET `/employees/`  
  Fetch all employees

- GET `/employees/{employee_id}`  
  Fetch one employee by ID

- PUT `/employees/{employee_id}`  
  Update employee details

- DELETE `/employees/{employee_id}`  
  Delete an employee

### Example Create Request

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "department": "Engineering",
  "salary": 75000
}
```

### Example Response

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com",
  "department": "Engineering",
  "salary": 75000.0
}
```

## Validation Rules

The API validates employee data using Pydantic:

- `name`: required, 2 to 100 characters
- `email`: must be a valid email format
- `department`: required, 2 to 100 characters
- `salary`: required and must be greater than 0

If a duplicate email is submitted, the API returns a conflict error.

## Database Model

The employee table is created automatically when the app starts using SQLAlchemy metadata:

- `id`: primary key
- `name`: employee name
- `email`: unique email address
- `department`: department name
- `salary`: employee salary

## Testing

The project includes basic API tests using FastAPI's TestClient and pytest.

Run tests with:

```bash
pytest
```

Current tests cover:

- root endpoint availability
- validation failure for invalid employee data

## Notes

This project is a good foundation for learning how to build a backend API with:

- FastAPI routing
- SQLAlchemy models and session handling
- Pydantic validation
- Postgres database integration
- CRUD patterns in a real application

You can extend it further with features like authentication, pagination, filtering, search, logging, and deployment configuration.

## License

This project is intended for learning and personal use.