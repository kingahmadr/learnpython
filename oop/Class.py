class Student:
    name: str
    age: str
    raport: float

    def __init__(self, name, age, raport):
        self.name = name
        self.age = age
        self.raport = raport

    def display_property(self):
        print(f"Student details:\nnama: {self.name}\nusia: {self.age}\nnilai raport: {self.raport}")

class School(Student):
    total_student = {}

    def __init__(self, name, age, raport, total_student):
        super().__init__(name=name, age=age, raport=raport)
        self.total_student = total_student

    def display(self):
        super().display_property()
        print(f"Total Student: {self.total_student}\n\n")

student_list = {}
for i in range(5):
    total_list_student = len(student_list)
    student_list[i] = School("Murid " + str(i), 28+i, 29.5+i, total_list_student)
    student_list[i].display()


        


