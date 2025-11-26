class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Welcome, {self.name}")
    
    def display_info(self):
        student_info = f"Student's name: {self.name} and age: {self.age}"
        return student_info
    
    def check_age(self):
        student_age = self.age
        try:
            if student_age < 16:
                print("No admission")
            else:
                print("Welcome")
        except TypeError:
            print("Student age must be a number.")

student1 = Student(age="14", name="John")
print(student1.display_info())
student1.check_age()