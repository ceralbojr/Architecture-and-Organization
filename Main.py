class Person:
    def __init__(self, id, lastName, firstName, middleName, type):
        self.id = id
        self.lastName = lastName
        self.firstName = firstName
        self.middleName = middleName
        self.type = type

    def getName(self):
        return self.lastName, self.firstName, self.middleName
class Student(Person):
    def __init__(selfid, lastName, firstName, middleName, type, course,):
        super