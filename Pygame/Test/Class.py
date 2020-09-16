# Classes

class Student:
    def __init__(self, firstName, lastName, grade: int):
        self.firstName = firstName
        self.lastName = lastName
        self.grade = grade
    def getName(self):
        return self.firstName + " " + self.lastName

ryan = Student("Ryan", "Wilson", 7)
mo = Student("Mo", "Khanal", 15)
print(ryan.getName())