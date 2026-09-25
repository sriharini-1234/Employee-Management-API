# Employee Management API

A FastAPI-based CRUD application for managing employee records using PostgreSQL and SQLAlchemy ORM.

## Technologies

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Swagger / OpenAPI
- Postman
- Pytest

## Features

- Create employee records
- View all employees
- View employee by ID
- Update employee details
- Delete employee records
- Request validation
- Email validation
- Salary validation
- Duplicate email handling
- PostgreSQL database integration
- Swagger API documentation
- Automated API testing

## Project Structure

```text
Employee Management API/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   │
│   └── routers/
│       ├── __init__.py
│       └── employees.py
│
├── tests/
│   ├── __init__.py
│   └── test_employees.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md