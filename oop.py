import  datetime
class Person:
    def __init__(self, name, age, hobby):
        self.name = name
        self.age =  age
        self.hobby =  hobby
    def yearofbirth(self):
        return datetime.date.today().year - self.age


class Astronaut(Person):
    def __init__(self, mission_count, position, training_hours, name, age, hobby):
        super().__init__(name, age, hobby)
        self.mission_count = mission_count
        self.position = position
        self.training_hours = training_hours

    def ageaftermission(self, missionduration):
        self.age += missionduration//12
        print(f"Age after this mission is: {self.age}")

p = Person("Jack Ryan", 32, "spying")

print(p.hobby)
print(p.name)
print(p.age)

print(f"{p.name} was born in {p.yearofbirth()}")

a = Astronaut(1,"Mission Commander", 1000, "Buzz", 34,"flight simulator")

print(a.__dict__.values())
a.ageaftermission(319)

