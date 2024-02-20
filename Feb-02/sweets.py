class Sweet:
    def __init__(self, brand, flavor, weight, is_vegan):
        self.brand = brand
        self.flavor = flavor
        self.weight = weight
        self.is_vegan = is_vegan
        self.is_wrapped = True

    def eat(self):
        if self.is_wrapped:
            print("Unwrap the candy before eating i t!")
        else:
            print("Enjoy your meal!")

    def unwrap(self):
        if self.is_wrapped:
            print(f"Unwrapped {self.flavor} candy from {self.brand}")
            self.is_wrapped = False
        else:
            print("The candy is unwrapped")

    def check_vegan(self):
        status = "vegan" if self.is_vegan else "not vegan"
        print(f"{self.brand} {self.flavor} candy is {status}.")

candy1 = Sweet("M&Ms", "Chocolate", 50, False)
candy2 = Sweet("Skittles", "Fruit", 40, True)

candy1.unwrap()
candy2.check_vegan()
candy1.eat()