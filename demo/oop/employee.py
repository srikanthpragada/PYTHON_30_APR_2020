from abc import ABC, abstractmethod


class Person(ABC):  # Abstract Base Class
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def print_details(self):
        print("Name     :", self.name)
        print("Email    :", self.email)

    def set_email(self, email):
        self.email = email

    def __str__(self):
        return f"{self.name},{self.email}"

    @abstractmethod
    def get_occupation(self):
        pass


class Employee(Person):
    def __init__(self, name, email, job, company):
        super().__init__(name, email)  # Call superclass's init
        self.job = job
        self.company = company

    def print_details(self):
        super().print_details()
        print("Job      :", self.job)
        print("Company  :", self.company)

    def __str__(self):
        return f"{super().__str__()},{self.job},{self.company}"

    def get_occupation(self):
        return f"Working as {self.job} in {self.company}"


class OverseasEmployee(Employee):
    def __init__(self, name, email, job, company, country):
        super().__init__(name, email, job, company)
        self.country = country

    def __str__(self):
        return f"{super().__str__()},{self.country}"


e = Employee("Jack", "jack@gmail.com", "Programmer", "Microsoft")
e.set_email("jack@yahoo.com")
print(e.get_occupation())

oe = OverseasEmployee("Mike", "mike@gmail.com", "DBA", "Oracle", "USA")
print(oe.get_occupation())
