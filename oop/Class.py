class Student:
    name: str
    age: str
    raport: float

    def __init__(self, name, age, raport):
        self.name = name
        self.age = age
        self.raport = raport

class School(Student):
    total_student = int

    def __init__(self, name, age, raport, total_student):
        super().__init__(name=name, age=age, raport=raport)
        self.total_student = total_student

    def display(self):
        print(f"Student details:\nnama: {self.name}\nusia: {self.age}\nnilai raport: {self.raport}\nTotal Student: {self.total_student}")


school_object = School("Andi", 28, 29.5, 30)
school_object.display()




        


