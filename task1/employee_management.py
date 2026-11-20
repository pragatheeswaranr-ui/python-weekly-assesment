
import csv
from pathlib import Path


# Read employee data from CSV file
file_path = Path(__file__).parent.parent / "data" / "employees.csv"

employees = []

try:
    with open(file_path, "r", newline="", encoding="utf-8-sig") as file:

        # Skip empty lines in CSV
        lines = (line for line in file if line.strip())

        reader = csv.DictReader(lines, skipinitialspace=True)

        # Clean CSV column names
        if reader.fieldnames:
            reader.fieldnames = [
                name.strip().lower() for name in reader.fieldnames
            ]

        print("CSV Headers:", reader.fieldnames)

        # Check required columns
        required_columns = {"id", "name", "department", "salary", "city"}

        if not reader.fieldnames or not required_columns.issubset(reader.fieldnames):
            raise ValueError("CSV file has missing or incorrect column names")

        for row in reader:

            if not row or not row.get("id"):
                continue

            row = {
                key.strip().lower(): value.strip()
                for key, value in row.items()
                if key is not None and value is not None
            }

            row["id"] = int(row["id"])
            row["salary"] = int(row["salary"])

            employees.append(row)

except FileNotFoundError:
    print("Error: employees.csv file not found")
    raise

except (ValueError, TypeError) as error:
    print("CSV Data Error:", error)
    raise


# 1. Bonus function
def bonus(salary, rate=0.1, *extras, **options):
    total = salary * rate + sum(extras)

    if "cap" in options:
        total = min(total, options["cap"])

    return total


print("\nBonus:", bonus(50000, 0.1, 1000, 500, cap=6000))


# 2. Custom exception
class InvalidSalaryError(Exception):
    pass


# 3. Employee class
class Employee:

    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")

        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"Employee: {self.name}, Salary: {self.salary}"


# 4. Manager class with inheritance
class Manager(Employee):

    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return (
            f"Manager: {self.name}, "
            f"Salary: {self.salary}, "
            f"Team Size: {self.team_size}"
        )


employee = Employee("Arun", 30000)
manager = Manager("Priya", 50000, 5)

print("\nEmployee Details:", employee.get_details())
print("Annual Salary:", employee.annual_salary())
print(manager.get_details())


# 5. Exception handling
try:
    invalid_employee = Employee("Test", -500)

except InvalidSalaryError as error:
    print("\nError:", error)

finally:
    print("Transaction finished")


# 6. List comprehension
above_50000 = [
    emp["name"] for emp in employees
    if emp["salary"] > 50000
]

print("\nAbove 50000:", above_50000)


# 7. Map and lambda
raised_salaries = list(
    map(lambda emp: round(emp["salary"] * 1.10, 2), employees)
)

print("After 10% raise:", raised_salaries)


# 8. Filter Chennai employees
chennai_employees = list(
    filter(lambda emp: emp["city"] == "Chennai", employees)
)

chennai_names = [
    emp["name"] for emp in chennai_employees
]

print("Chennai:", chennai_names)


# 9. For loop with continue and break
print("\nSalary Loop:")

for emp in employees:
    salary = emp["salary"]

    if salary == 0:
        continue

    if salary > 85000:
        print("Salary above 85000 found. Stopping loop.")
        break

    print(emp["name"], salary)


# 10. Write results into a text file
output_path = Path(__file__).parent / "employee_summary.txt"

with open(output_path, "w", encoding="utf-8") as file:
    file.write("Employee Analysis Summary\n")
    file.write("=========================\n")
    file.write(f"Employees above 50000: {above_50000}\n")
    file.write(f"Chennai employees: {chennai_names}\n")
    file.write(f"Raised salaries: {raised_salaries}\n")

print("\nSummary saved successfully!")
