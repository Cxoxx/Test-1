#parent class
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"

    def speak(self):
        return f"{self.name} says: Hello!"

#child class:student
class Student(Person):
    def __init__(self, name, age, address, student_id, major):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.major = major

    def get_details(self):
        parent_details = super().get_details()
        return f"{parent_details}, Student ID: {self.student_id}, Major: {self.major}"

    def study(self):
        return f"{self.name} is studying {self.major}."

#child class:Teacher
class Teacher(Person):
    def __init__(self, name, age, address, employee_id, subject):
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.subject = subject

    def get_details(self):
        parent_details = super().get_details()
        return f"{parent_details}, Employee ID: {self.employee_id}, Subject: {self.subject}"

    def teach(self):
        return f"{self.name} is teaching {self.subject}."
