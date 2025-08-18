

#exercice 3

import random



class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if my_power > other_power:
            return f"{self.name} won the fight!"
        elif my_power < other_power:
            return f"{other_dog.name} won the fight!"
        else:
            return "It’s a draw!"

class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dogs = [self.name] + [dog.name for dog in args]
        print(f"{', '.join(dogs)} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained yet!")


# --- Saisie utilisateur ---
name = input("\nNom du chien domestique : ")
age = int(input(f"Âge de {name} : "))
weight = float(input(f"Poids de {name} (kg) : "))
my_dog = PetDog(name, age, weight)

my_dog.train()
my_dog.do_a_trick()

