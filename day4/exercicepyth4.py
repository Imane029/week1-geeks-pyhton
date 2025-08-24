class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())
#exercice 1

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# --- Saisie utilisateur ---
all_cats = []
for breed in [Bengal, Chartreux, Siamese]:
    name = input(f"Entrez le nom du chat {breed.__name__} : ")
    age = int(input(f"Entrez l'âge de {name} : "))
    all_cats.append(breed(name, age))

sara_pets = Pets(all_cats)

print("\nTous les chats sortent en promenade 🐾")
sara_pets.walk()

#exercice 2

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


# --- Saisie utilisateur ---
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


#exercice 2
        
dogs = []
for i in range(3):
    name = input(f"\nNom du chien {i+1} : ")
    age = int(input(f"Âge de {name} (en années) : "))

    
    weight_input = input(f"Poids de {name} (en kg, ex: 2.5 ou 7kg) : ")
    weight_input = weight_input.lower().replace("kg", "").strip()  
    weight = float(weight_input)  

    dogs.append(Dog(name, age, weight))

print("\n👉 Test des chiens :")
print(dogs[0].bark())
print(f"La vitesse de {dogs[1].name} est {dogs[1].run_speed():.2f}")
print(dogs[2].fight(dogs[0]))

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



name = input("\nNom du chien domestique : ")
age = int(input(f"Âge de {name} : "))

# Nettoyer l'entrée de poids pour accepter "12" ou "12kg"
weight_input = input(f"Poids de {name} (kg) : ")
weight = float(weight_input.replace("kg", "").strip())

my_dog = PetDog(name, age, weight)


my_dog.train()
my_dog.do_a_trick()

#exercice 4

class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f'Félicitations à la famille {self.last_name} pour le nouveau-né !')

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f'Famille {self.last_name}')
        for member in self.members:
            print(f"Nom: {member['name']}, Âge: {member['age']}, Genre: {member['gender']}, Est un enfant: {member['is_child']}")


nom_famille = input("Entrez le nom de famille : ")
membres = []
nombre_membres = int(input("Combien de membres dans la famille ? "))
for i in range(nombre_membres):
    nom = input(f"Entrez le nom du membre {i+1} : ")
    age = int(input(f"Entrez l'âge de {nom} : "))
    genre = input(f"Entrez le genre de {nom} : ")
    est_enfant = input(f"Est-ce que {nom} est un enfant ? (oui/non) : ").lower() == 'oui'
    membres.append({'name': nom, 'age': age, 'gender': genre, 'is_child': est_enfant})

ma_famille = Family(nom_famille, membres)
ma_famille.family_presentation()


nom_bebe = input("Entrez le nom du nouveau-né : ")
genre_bebe = input(f"Entrez le genre de {nom_bebe} : ")
ma_famille.born(name=nom_bebe, age=0, gender=genre_bebe, is_child=True)
ma_famille.family_presentation()


#exercice 5
class TheIncredibles(Family):
    def __init__(self, last_name, members):
        super().__init__(last_name, members)

    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{member['incredible_name']} utilise son pouvoir : {member['power']}")
                else:
                    raise Exception(f"{name} n'a pas plus de 18 ans et ne peut pas utiliser son pouvoir !")

    def incredible_presentation(self):
        print("Voici notre puissante famille !")
        super().family_presentation()


nom_famille = 'Incroyables'
membres_incroyables = []
nombre_membres = int(input("Combien de membres dans la famille Incroyables ? "))
for i in range(nombre_membres):
    nom = input(f"Entrez le nom du membre {i+1} : ")
    age = int(input(f"Entrez l'âge de {nom} : "))
    genre = input(f"Entrez le genre de {nom} : ")
    est_enfant = input(f"Est-ce que {nom} est un enfant ? (oui/non) : ").lower() == 'oui'
    pouvoir = input(f"Entrez le pouvoir de {nom} : ")
    nom_incroyable = input(f"Entrez le nom d'incroyable de {nom} : ")
    membres_incroyables.append({
        'name': nom,
        'age': age,
        'gender': genre,
        'is_child': est_enfant,
        'power': pouvoir,
        'incredible_name': nom_incroyable
    })

famille_incredibles = TheIncredibles(nom_famille, membres_incroyables)
famille_incredibles.incredible_presentation()


nom_bebe = input("Entrez le nom du nouveau-né incroyable : ")
genre_bebe = input(f"Entrez le genre de {nom_bebe} : ")
pouvoir_bebe = input(f"Entrez le pouvoir de {nom_bebe} : ")
nom_incroyable_bebe = input(f"Entrez le nom d'incroyable de {nom_bebe} : ")
famille_incredibles.born(name=nom_bebe, age=0, gender=genre_bebe, is_child=True, power=pouvoir_bebe, incredible_name=nom_incroyable_bebe)

famille_incredibles.incredible_presentation()
