

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


def create_dog():
    name = input("Entrez le nom du chien : ")
    age = int(input("Entrez l'âge du chien (en années) : "))
    weight_input = input("Entrez le poids du chien (ex: 12 ou 12kg) : ")
    
    weight = float(''.join(filter(lambda x: x.isdigit() or x=='.', weight_input)))
    return Dog(name, age, weight)


all_dogs = []

num = int(input("Combien de chiens voulez-vous ajouter ? "))

for i in range(num):
    print(f"\nCréation du chien #{i+1}")
    dog = create_dog()
    all_dogs.append(dog)


print("\nRésultats des chiens :")
for dog in all_dogs:
    print(f"\nNom : {dog.name}")
    print(f"Age : {dog.age} ans, Poids : {dog.weight} kg")
    print(dog.bark())
    print(f"Vitesse de course : {dog.run_speed():.2f}")


if len(all_dogs) > 1:
    first_dog = all_dogs[0]
    for opponent in all_dogs[1:]:
        print(f"\nCombat : {first_dog.name} vs {opponent.name}")
        print(first_dog.fight(opponent))
