from abc import ABC, abstractmethod
class Vechicle(ABC):
    @abstractmethod
    def start_range(self):
        pass
class Car(Vechicle):
    def start_range(self):
        print("car started")
car1=Car()
car1.start_range()