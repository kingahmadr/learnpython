# class Student:
#     name: str
#     age: str
#     raport: float

#     def __init__(self, name, age, raport):
#         self.name = name
#         self.age = age
#         self.raport = raport

#     def display_property(self):
#         print(f"Student details:\nnama: {self.name}\nusia: {self.age}\nnilai raport: {self.raport}")

# class School(Student):
#     total_student = {}

#     def __init__(self, name, age, raport, total_student):
#         super().__init__(name=name, age=age, raport=raport)
#         self.total_student = total_student

#     def display(self):
#         super().display_property()
#         print(f"Total Student: {self.total_student}\n\n")

# student_list = {}
# for i in range(5):
#     total_list_student = len(student_list)
#     student_list[i] = School("Murid " + str(i), 28+i, 29.5+i, total_list_student)
#     student_list[i].display()

class School:
    def __init__(self, students):
        self.students = students  

    def display_student(self):
        total_student = []
        for student in self.students:
            student.display() 
            print("")
            total_student.append(student)
        print(f"Total All Students in list: {len(total_student)}")

class Student:
    def __init__(self, name, age, raport):
        self.name = name
        self.age = age
        self.raport = raport

    def display(self):
        print(f"Student details:\nName: {self.name}\nAge: {self.age}\nRaport: {self.raport}")

school_object = School({"ani", 29, 28})
print(school_object.display_student)

student1 = Student("Ani", 18, 85.6)
student2 = Student("Tokek", 16, 90.1)
student3 = Student("Cicak", 20, 90.1)
student4 = Student("Bubi", 21, 90.2)
student5 = Student("Babi", 22, 90.4)

school_object = School([student1, student2, student3, student4])

school_object.display_student()


        


