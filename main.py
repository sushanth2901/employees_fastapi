from fastapi import FastAPI, HTTPException
import json
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Define the Employee model
class Employee(BaseModel):
    emp_id: int
    name: str
    salary: float
    address: str

# Helper function to read data from the JSON file
def read_employees():
    try:
        with open("employees.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Helper function to write data to the JSON file
def write_employees(employees):
    with open("employees.json", "w") as file:
        json.dump(employees, file, indent=4)
# json.dump --> converts your list/dict into JSON string and dumps this to a file
# employees --> List
# file --> Alias to employees.json

# API to register a new employee
@app.post("/employees/", response_model=Employee)
def register_employee(employee: Employee):
    employees = read_employees()

    # Check if employee ID already exists
    for emp in employees:
        if emp["emp_id"] == employee.emp_id:
            raise HTTPException(status_code=400, detail="Employee ID already exists")

    employees.append(employee.dict())
    write_employees(employees)
    return employee


# API to get an employee by ID
@app.get("/employees/{emp_id}", response_model=Employee)
def get_employee(emp_id: int):
    employees = read_employees()
    for emp in employees:
        if emp["emp_id"] == emp_id:
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")


# API to delete an employee by ID
@app.delete("/employees/{emp_id}", response_model=dict)
def delete_employee(emp_id: int):
    employees = read_employees()
    for emp in employees:
        if emp["emp_id"] == emp_id:
            employees.remove(emp)
            write_employees(employees)
            return {"message": "Employee deleted successfully"}
    raise HTTPException(status_code=404, detail="Employee not found")


# API to get all employees
@app.get("/employees/", response_model=List[Employee])
def get_all_employees():
    return read_employees()