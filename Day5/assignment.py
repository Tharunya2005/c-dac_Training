class InvalidSalaryError(Exception):
    """Raised when salary is invalid (<= 0)."""
    pass

class Person:
    def __init__(self, name: str, city: str):
        self.name = name
        self.city = city

    def get_details(self) -> str:
        return f"Name: {self.name}, City: {self.city}"

class Employee(Person):

    company_name = "Vinod Technologies"

    def __init__(self, emp_id: str, name: str, city: str, salary: float):
        super().__init__(name, city)

        if not Employee.is_valid_salary(salary):
            raise InvalidSalaryError("Salary must be greater than 0.")

        self.emp_id = emp_id
        self.__salary = salary  

    @staticmethod
    def is_valid_salary(salary: float) -> bool:
        return salary > 0

    def get_salary(self) -> float:
        return self.__salary

    def update_salary(self, new_salary: float) -> None:
        if not Employee.is_valid_salary(new_salary):
            raise InvalidSalaryError("Updated salary must be greater than 0.")
        self.__salary = new_salary

    def get_details(self) -> str:
        return (
            f"Company: {Employee.company_name}\n"
            f"Employee ID: {self.emp_id}\n"
            f"Name: {self.name}\n"
            f"City: {self.city}\n"
            f"Salary: {self.__salary}"
        )

    def __add__(self, other):
        if not isinstance(other, Employee):
            raise TypeError("Addition allowed only between Employee objects.")
        return self.__salary + other.__salary


    def __str__(self):
        return f"{self.emp_id} - {self.name} ({self.city}) | Salary: {self.__salary}"

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.emp_id == other.emp_id
        return False

    @classmethod
    def change_company_name(cls, new_name: str):
        cls.company_name = new_name

def main():
    try:
        # Creating Employees
        emp1 = Employee("E101", "Arun", "Bangalore", 50000)
        emp2 = Employee("E102", "Divya", "Chennai", 60000)

        # Printing Details
        print("---- Employee Details ----")
        print(emp1.get_details())
        print()
        print(emp2.get_details())

        # Updating Salary
        print("\n---- Updating Salary ----")
        emp1.update_salary(55000)
        print(f"Updated Salary of {emp1.emp_id}: {emp1.get_salary()}")

        # Operator Overloading
        print("\n---- Adding Salaries ----")
        total_salary = emp1 + emp2
        print(f"Total Salary of emp1 and emp2: {total_salary}")

        # Demonstrating Inheritance
        print("\n---- Inheritance Check ----")
        print(emp1.get_details())

        # Accessing Static Member
        print("\n---- Company Name ----")
        print(Employee.company_name)

        # Changing Company Name (Bonus)
        Employee.change_company_name("Vinod Global Tech")
        print("Updated Company Name:", Employee.company_name)

        # Triggering Custom Exception
        print("\n---- Trigger Invalid Salary ----")
        emp3 = Employee("E103", "Ravi", "Mumbai", -10000)

    except InvalidSalaryError as e:
        print("Custom Exception Caught:", e)

    except TypeError as e:
        print("Type Error:", e)


if __name__ == "__main__":
    main()