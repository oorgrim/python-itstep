
import math

def calculate_tank_volume(diameter, height):
    radius = diameter / 2
    base_area = math.pi * radius**2
    volume_cubic_meters = base_area * height #формулв объема = площаль основания на высоту. 
    volume_liters = volume_cubic_meters * 1000 #преобразовала
    return volume_liters


try:
    diameter = int(input('введите диаметр: ')) 
    height = int(input('введите высоту: '))

except ValueError:
    print('введите число!')

else:
    tank_volume = calculate_tank_volume(diameter, height)
    print(f"Объем бака: {tank_volume} литров")