class Dog:
    def __init__(self):
        print("name")
    def fruits(self):
        print("name1")

class Fruits(Dog):
    def __init__(self):
        super().__init__()
        self.fruits()
s1=Dog()
s1.fruits()
s2=Fruits()
