class Fan:
    slow = 1
    medium = 2
    fast = 3

    def __init__(self, initial_speed=slow, initial_radius=5.0, initial_color="blue", initial_on_status=False):
        self.__speed = initial_speed
        self.__radius = float(initial_radius)
        self.__color = str(initial_color)
        self.__on_status = bool(initial_on_status)

    #getter method for speed
    def get_speed(self):
        return self.__speed

    #setter method for speed
    def set_speed(self, new_speed):
        self.__speed = new_speed

    #getter method for radius
    def get_radius(self):
        return self.__radius

    #setter method for radius
    def set_radius(self, new_radius):
        self.__radius = float(new_radius)

    #getter method for color
    def get_color(self):
        return self.__color

    #setter method for color
    def set_color(self, new_color):
        self.__color = str(new_color)

    #getter method for power status
    def get_on_status(self):
        return self.__on_status

    #setter method for power status
    def set_on_status(self, new_on_status):
        self.__on_status = bool(new_on_status)

class TestFan:
    #method to run the test
    def run_test(self):
        #creating first object of the class
        first_fan = Fan()

        #changing speed using setter
        first_fan.set_speed(Fan.fast)
        #changing radius using setter
        first_fan.set_radius(10.0)
        #changing color using setter
        first_fan.set_color("yellow")
        #changing power status using setter
        first_fan.set_on(True)

        #creating second object of the class
        second_fan = Fan()

        #changing speed using setter
        second_fan.set_speed(Fan.medium)
        #changing radius using setter
        second_fan.set_radius(5.0)
        #changing color using setter
        second_fan.set_color("blue")
        #changing power status using setter
        second_fan.set_on(False)



