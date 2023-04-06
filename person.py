class Person:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender.upper()

    def __str__(self):
        return "Name; " + self.name + "\nGender; " + self.gender
