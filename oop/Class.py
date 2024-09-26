class School:
    def __init__(self, students):
        self.students = students  

    def display_student(self):
        for student in self.students:
            student.display() 
            print("")
        print(f"Total All Students in list: {len(self.students)}")

class Student:
    def __init__(self, name, age, raport):
        self.name = name
        self.age = age
        self.raport = raport

    def display(self):
        print(f"Student details:\nName: {self.name}\nAge: {self.age}\nRaport: {self.raport}")

student1 = Student("Ani", 18, 85.6)
student2 = Student("Tokek", 16, 90.1)
student3 = Student("Cicak", 20, 90.1)
student4 = Student("Bubi", 21, 90.2)
student5 = Student("Babi", 22, 90.4)

school_object = School([student1, student2, student3, student4, student5])

school_object.display_student()