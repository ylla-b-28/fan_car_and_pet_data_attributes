class Car:
    def __init__(self, year_model, make):
        self.__year_model = str(year_model)
        self.__make = str(make)
        self.__speed = 0

    #method to add 5 to the speed attribute
    def accelerate(self):
        self.__speed += 5

    #method to subtract 5 from the speed attribute
    def brake(self):
        if self.__speed >= 5:
            self.__speed -= 5
        else:
            self.__speed = 0

    #getter method for current speed
    def get_speed(self):
        return self.__speed

    #getter method for year model
    def get_year_model(self):
        return self.__year_model

    #getter method for make
    def get_make(self):
        return self.__make

class TestCar:
    #method to display car's details
    def display_car_properties(self, car_object, car_display_name, action_type):
        print(f"\033[1;95m₊˚ ✧ ━━━━ ⊱\033[0m \033[1;38;5;129m{car_display_name}\033[0m \033[1;95m⊰ ━━━━ ✧ ₊˚\033[0m")

        year_model_value = car_object.get_year_model()
        make_value = car_object.get_make()
        speed_value = car_object.get_speed()








