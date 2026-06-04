class Fan:
    slow = 1
    medium = 2
    fast = 3

def __init__(self, initial_speed=slow, initial_radius=5.0, initial_color="blue", initial_on_status=False):
    self.__speed = initial_speed
    self.__radius = float(initial_radius)
    self.__color = str(initial_color)
    self.__on_status = bool(initial_on_status)

