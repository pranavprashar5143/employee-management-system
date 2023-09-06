class EmployeeManagementSystem:
    def _init_(self):
        self.employees = {}

    def add_employee(self, emp_id, emp_name, emp_salary):
        if emp_id not in self.employees:
            self.employees[emp_id] = {'name': emp_name, 'salary': emp_salary}
            print(f'Employee {emp_name} added successfully.')
        else:
            print(f'Employee with ID {emp_id} already exists.')

    def remove_employee(self, emp_id):
        if emp_id in self.employees:
            emp_name = self.employees[emp_id]['name']
            del self.employees[emp_id]
            print(f'Employee {emp_name} removed successfully.')
        else:
            print(f'Employee with ID {emp_id} not found.')

    def list_employees(self):
        print("Employee List:")
        for emp_id, emp_info in self.employees.items():
            print(f'ID: {emp_id}, Name: {emp_info["name"]}, Salary: {emp_info["salary"]}')

# Create an instance of the EmployeeManagementSystem
ems = EmployeeManagementSystem()

while True:
    print("\nOptions:")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. List Employees")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        emp_id = input("Enter employee ID: ")
        emp_name = input("Enter employee name: ")
        emp_salary = input("Enter employee salary: ")
        ems.add_employee(emp_id, emp_name, emp_salary)
    elif choice == '2':
        emp_id = input("Enter employee ID to remove: ")
        ems.remove_employee(emp_id)
    elif choice == '3':
        ems.list_employees()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please select a valid option.")