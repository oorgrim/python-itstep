from animal import Animal

class Predator(Animal):
    def init(self, name, weight, size):
        super().init(name, weight, size)
        self.prey_eaten = set()
    
    def eat(self, prey):
        if isinstance(prey, Animal) and prey.alive and prey.size < self.size and prey not in self.prey_eaten:
            self.size += prey.size * 0.2
            self.weight += prey.weight * 0.2
            prey.alive = False
            self.prey_eaten.add(prey)