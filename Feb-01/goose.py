from herbivore import Herbivore

class Goose(Herbivore):
    def __init__(self, name, weight, size):
        super().__init__(name, weight, size, ["grass", "plants"])
    
    def talk(self):
        print("Mmmm")
