class Person:
    """Creating base class for human."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        """Return short description of person."""
        return print("My name is {}, I am {}".format(self.name, self.age))

class Adult(Person):
    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.job = job

    def bio(self):
        """Return short description of adult instance."""
        return print("My name is {}, I am {}, and I work as a {}.".format(self.name, self.age, self.job))

mary = Person("mary", 12)
print(mary.name)
mary.info()

joe = Adult("Joe", 41, "cook")
print(joe.job)
joe.bio()

