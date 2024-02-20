class Headphones:
    def __init__(self, brand, model, color, wireless):
        self.brand = brand
        self.model = model
        self.color = color
        self.wireless = wireless
        self.volume = 50

    def adjust_volume(self, delta):
        self.volume = max(0, min(100, self.volume + delta))
        print(f"Adjusted volume to {self.volume}")

    def play_music(self, song):
        print(f"Now playing: {song}")

    def toggle_wireless(self):
        self.wireless = not self.wireless
        status = "enabled" if self.wireless else "disabled"
        print(f"Wirelss mode is now {status}")

headphones1 = Headphones("Sony", "WH-1000XM4", "Black", True)
headphones2 = Headphones("Apple", "AirPods Pro", "White", True)

headphones1.adjust_volume(10)
headphones2.play_music("Winter - Antonio Vivaldi")
headphones1.toggle_wireless()
