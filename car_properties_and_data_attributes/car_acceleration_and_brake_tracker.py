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

        if action_type == "Accelerating":
            power_state_value = "\033[1;92m"
            power_status_text_label = "Accelerating"
        elif action_type == "Braking":
            power_state_value = "\033[1;91m"
            power_status_text_label = "Braking"
        else:
            power_state_value = "\033[0m"
            power_status_text_label = "Stationary"

        print(f"   Year Model: {year_model_value}")
        print(f"   Make:       {make_value}")
        print(f"   Speed:      \033[1;38;5;129m{speed_value}\033[0m")
        print(f"   Status:     {power_state_value}{power_status_text_label}\033[0m")

    def run_test(self):
        porsche_car = Car(2026, "Porsche 911 GT3 RS")

        # Accelerate 1
        porsche_car.accelerate()
        print("")
        self.display_car_properties(porsche_car, "First Accelerate", "Accelerating")
        print("\033[1;95m⊱.˚── ⋅ .✧˚❀˚✧. ⋅ ──˚.⊰\033[0m")

        # Accelerate 2
        porsche_car.accelerate()
        print("")
        self.display_car_properties(porsche_car, "Second Accelerate", "Accelerating")
        print("\033[1;95m⊱.˚── ⋅ .✧˚❀˚✧. ⋅ ──˚.⊰\033[0m")

        # Accelerate 3
        porsche_car.accelerate()
        print("")
        self.display_car_properties(porsche_car, "Third Accelerate", "Accelerating")
        self.display_car_properties(porsche_car, "Third Accelerate", "Accelerating")

        # Accelerate 4
        porsche_car.accelerate()
        print("")
        self.display_car_properties(porsche_car, "Fourth Accelerate", "Accelerating")
        print("\033[1;95m⊱.˚── ⋅ .✧˚❀˚✧. ⋅ ──˚.⊰\033[0m")

        # Accelerate 5
        porsche_car.accelerate()
        print("")
        self.display_car_properties(porsche_car, "Fifth Accelerate", "Accelerating")
        print("\033[1;95m⊱.˚── ⋅ .✧˚❀˚✧. ⋅ ──˚.⊰\033[0m")

        # Brake 1
        porsche_car.brake()
        print("")
        self.display_car_properties(porsche_car, "First Brake", "Braking")
        print("\033[1;95m⊱.˚── ⋅ .✧˚❀˚✧. ⋅ ──˚.⊰\033[0m")

        # Brake 2
        porsche_car.brake()
        print("")
        self.display_car_properties(porsche_car, "Second Brake", "Braking")
        print("\033[1;95m⊱.˚── ⋅ .✧˚❀˚✧. ⋅ ──˚.⊰\033[0m")

        # Brake 3
        porsche_car.brake()
        print("")
        self.display_car_properties(porsche_car, "Third Brake", "Braking")
        print("\033[1;95m⊱.˚── ⋅ .✧˚❀˚✧. ⋅ ──˚.⊰\033[0m")

        # Brake 4
        porsche_car.brake()
        print("")
        self.display_car_properties(porsche_car, "Fourth Brake", "Braking")
        print("\033[1;95m⊱.˚── ⋅ .✧˚❀˚✧. ⋅ ──˚.⊰\033[0m")

        # Brake 5
        porsche_car.brake()
        print("")
        self.display_car_properties(porsche_car, "Fifth Brake", "Braking")
        print("\033[1;95m⊱.˚── ⋅ .✧˚❀˚✧. ⋅ ──˚.⊰\033[0m")

        # System Diagnostics Footer
        print("\n          \033[1;96m⋆⁺｡˚⋆˙‧₊☽ ◯ ☾₊‧˙⋆˚｡⁺⋆\033[0m")
        print("  \033[1;92mSystem diagnostics completed successfully.\033[0m")
        print("          \033[1;96m⋆⁺｡˚⋆˙‧₊☽ ◯ ☾₊‧˙⋆˚｡⁺⋆\033[0m\n")

if __name__ == "__main__":
    test_execution = TestCar()
    test_execution.run_test()
