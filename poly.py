class car:
    def sound(self):
        print("first sound")
class bus:
    def sound(self):
        print("Second sound")
def make_sounds(vechicle):
    vechicle.sound()
make_sounds(car())
make_sounds(bus())
