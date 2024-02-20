class Keyboard:
    def __init__(self, brand, model, layout, wireless):
        self.brand = brand
        self.model = model
        self.layout = layout
        self.wireless = wireless
        self.is_backlit = False

    def press_key(self, key):
        print(f"Pressed key: {key}")

    def change_backlit(self, backlit_color):
        if self.is_backlit:
            print(f"Changed backlit color to {backlit_color}")
        else:
            print("This keyboard is not bcklit") #подсветка

    def toggle_wireless(self):
        self.wireless = not self.wireless
        status = "enabled" if self.wireless else "disabled"
        print(f"Wireless mode is now {status}")

keyboard1 = Keyboard("Logitech", "g102", "QWERTY", True)
keyboard2 = Keyboard("Razer", "BlackWidow V3", "AZERTY", False)

keyboard1.press_key("A")
keyboard2.change_backlit("Blue")
keyboard1.toggle_wireless()
