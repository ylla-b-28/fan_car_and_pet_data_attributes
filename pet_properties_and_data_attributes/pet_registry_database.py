class Pet:
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    def set_name(self, name):
        self.__name = str(name)

    def set_animal_type(self, animal_type):
        self.__animal_type = str(animal_type)

    def set_age(self, age):
        self.__age = int(age)

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

class TestPet:
    def display_pet_properties(self, pet_object, pet_display_name):
        print(f"\033[1;95m₊˚ ✧ ━━━━ ⊱\033[0m \033[1;38;5;129m{pet_display_name}\033[0m \033[1;95m⊰ ━━━━ ✧ ₊˚\033[0m")

        name_value = pet_object.get_name()
        type_value = pet_object.get_animal_type()
        age_value = pet_object.get_age()

        power_state_value = "\033[1;92m"
        power_status_text_label = "Registered"

        print(f"   \033[1;38;5;208mPet Name:\033[0m    \033[1;92m{name_value}\033[0m")
        print(f"   \033[1;38;5;208mAnimal Type:\033[0m \033[1;93m{type_value}\033[0m")
        print(f"   \033[1;38;5;208mPet Age:\033[0m     \033[1;38;5;129m{age_value}\033[0m")
        print(f"   \033[1;38;5;208mStatus:\033[0m      {power_state_value}{power_status_text_label}\033[0m")

    def run_test(self):
        my_pet = Pet()

        print("")
        user_name = input("\033[1;38;5;208mEnter your pet's name:\033[0m ")
        user_type = input("\033[1;38;5;208mEnter your pet's animal type (e.g., Dog, Cat, Bird):\033[0m ")
        user_age = input("\033[1;38;5;208mEnter your pet's age:\033[0m ")

        my_pet.set_name(user_name)
        my_pet.set_animal_type(user_type)
        my_pet.set_age(user_age)

        print("")
        self.display_pet_properties(my_pet, "Pet Profile Object")
        print("\033[1;95m⊱.˚── ⋅ .✧˚❀˚✧. ⋅ ──˚.⊰\033[0m")