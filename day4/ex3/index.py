
import random


class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        if my_power > other_power:
            return f"{self.name} won the fight!"
        elif my_power < other_power:
            return f"{other_dog.name} won the fight!"
        else:
            return "It's a tie!"


class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True
        print(f"{self.name} is now trained!")

    def play(self, *args):
        names = [self.name] + [dog.name for dog in args]
        print(f"{', '.join(names)} all play together!")

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
            print(f"{self.name} is not trained yet. Train first!")

def create_petdog():
    name = input("Entrez le nom du chien : ")
    age = int(input("Entrez l'âge du chien (en années) : "))
    weight_input = input("Entrez le poids du chien (ex: 12 ou 12kg) : ")
    weight = float(''.join(filter(lambda x: x.isdigit() or x=='.', weight_input)))
    return PetDog(name, age, weight)

all_dogs = []

num = int(input("Combien de chiens voulez-vous ajouter ? "))

for i in range(num):
    print(f"\nCréation du chien #{i+1}")
    dog = create_petdog()
    all_dogs.append(dog)


while True:
    print("\n--- Menu ---")
    print("1 - Entraîner un chien")
    print("2 - Jouer avec les chiens")
    print("3 - Faire un tour")
    print("4 - Afficher info chiens")
    print("0 - Quitter")
    choice = input("Choisissez une option : ")

    if choice == "1":
        for idx, dog in enumerate(all_dogs):
            print(f"{idx+1} - {dog.name}")
        sel = int(input("Quel chien voulez-vous entraîner ? ")) - 1
        all_dogs[sel].train()

    elif choice == "2":
        for idx, dog in enumerate(all_dogs):
            print(f"{idx+1} - {dog.name}")
        sel_list = input("Entrez les numéros des chiens à faire jouer (ex: 1 2) : ")
        indices = [int(x)-1 for x in sel_list.split()]
        selected_dogs = [all_dogs[i] for i in indices]
        selected_dogs[0].play(*selected_dogs[1:])

    elif choice == "3":
        for idx, dog in enumerate(all_dogs):
            print(f"{idx+1} - {dog.name}")
        sel = int(input("Quel chien doit faire un tour ? ")) - 1
        all_dogs[sel].do_a_trick()

    elif choice == "4":
        print("\nInfos chiens :")
        for dog in all_dogs:
            print(f"{dog.name}, Age: {dog.age}, Poids: {dog.weight}, Trained: {dog.trained}")

    elif choice == "0":
        print("Au revoir !")
        break

    else:
        print("Option invalide. Réessayez.")
