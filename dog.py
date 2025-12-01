class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_details(self):
        print(f"This is the name of animal : {self.name} with the age is : {self.age}")
class Lion(Animal): # Single inheritance
    def sound(self):
        self.display_details()
class Cat(Lion): # Multilevel inheritance
    def make_sound(self):
        self.sound()
a=Cat("Samba",5)
a.make_sound()
# Multiple inheritance
class Friendly:
    def greet(self):
        print("Friendly!")
class group_animals(Friendly,Lion):
    def make_group(self):
        self.display_details
w=group_animals("akanksha",16)
w.display_details()