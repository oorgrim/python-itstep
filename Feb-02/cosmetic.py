class Cosmetic:
    def __init__(self, brand, product_type, shade, is_opened):
        self.brand = brand
        self.product_type = product_type
        self.shade = shade
        self.is_opened = is_opened
        self.is_opened = False

    def apply(self):
        if self.is_opened:
            print(f"Applying {self.shade} {self.product_type} by {self.brand}")
        else:
            print("Cannot apply, the product isnt opened")

    def open_container(self):
        if not self.is_opened:
            print(f"Opened {self.product_type} by {self.brand}")
            self.is_opened = True
        else:
            print("The container is opened")

    def structure(self):
        print(f"{self.brand} {self.product_type} in {self.shade} shade has a unique formulation!!!")

cosmetic1 = Cosmetic("Dior", "lipstick", "Ruby", True)
cosmetic2 = Cosmetic("Maybelline", "eyeshadow", "someone", False)

cosmetic1.open_container()
cosmetic1.apply()
cosmetic2.structure()