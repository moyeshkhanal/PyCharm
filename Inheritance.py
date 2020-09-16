# Inheritance

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year=2020):
        super().__init__(fname, lname)
        self.graduatingYear = year

    def getYear(self):
        print(self.graduatingYear)

    def printname(self):
        print("Student", self.firstname, self.lastname)


class Example(Student, Person):
    def __init__(self, fname, lname, year, gpa):
        Student.__init__(self, fname, lname, year)


x = Person("John", "Doe")
x.printname()

