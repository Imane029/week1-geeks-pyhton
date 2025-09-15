
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    pass

class Chartreux(Cat):
    pass

class Siamese(Cat):
    pass

class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


def create_cat():
    name = input("Entrez le nom du chat : ")
    age = int(input("Entrez l'âge du chat : "))
    print("Choisissez la race du chat :")
    print("1 - Bengal")
    print("2 - Chartreux")
    print("3 - Siamese")
    race_choice = input("Entrez 1, 2 ou 3 : ")

    if race_choice == "1":
        return Bengal(name, age)
    elif race_choice == "2":
        return Chartreux(name, age)
    else:
        return Siamese(name, age)


all_cats = []

num = int(input("Combien de chats voulez-vous ajouter ? "))

for i in range(num):
    print(f"\nCréation du chat #{i+1}")
    cat = create_cat()
    all_cats.append(cat)

sara_pets = Pets(all_cats)
print("\nLes chats se promènent :")
sara_pets.walk()
