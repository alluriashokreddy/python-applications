class Employee:
    name: str
    age: int
    salary: int

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


class Company:
    employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def get_employee_count(self):
        return len(self.employees)
