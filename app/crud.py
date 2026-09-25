from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from . import models
from .schemas import EmployeeCreate


def create_employee(
    db: Session,
    employee: EmployeeCreate
):
    new_employee = models.Employee(
        name=employee.name,
        email=employee.email,
        department=employee.department,
        salary=employee.salary
    )

    db.add(new_employee)

    try:
        db.commit()
        db.refresh(new_employee)
    except IntegrityError:
        db.rollback()
        raise

    return new_employee


def get_employees(db: Session):
    return db.query(models.Employee).all()


def get_employee(
    db: Session,
    employee_id: int
):
    return (
        db.query(models.Employee)
        .filter(models.Employee.id == employee_id)
        .first()
    )


def update_employee(
    db: Session,
    employee_id: int,
    employee: EmployeeCreate
):
    existing_employee = get_employee(db, employee_id)

    if existing_employee is None:
        return None

    existing_employee.name = employee.name
    existing_employee.email = employee.email
    existing_employee.department = employee.department
    existing_employee.salary = employee.salary

    try:
        db.commit()
        db.refresh(existing_employee)
    except IntegrityError:
        db.rollback()
        raise

    return existing_employee


def delete_employee(
    db: Session,
    employee_id: int
):
    existing_employee = get_employee(db, employee_id)

    if existing_employee is None:
        return None

    db.delete(existing_employee)
    db.commit()

    return existing_employee