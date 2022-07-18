class Person:
    def __init__(self, first_name, last_name, age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


me = Person("Ralitsa", "Kaneva", 32)

print(me.get_full_name())
