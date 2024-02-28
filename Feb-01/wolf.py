from predator import Predator

class Wolf(Predator):
    def init(self, name, weight, size):
        super().__init__(name, weight, size)
    
    def talk(self):
        print("Woof!")