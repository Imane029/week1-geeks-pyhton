
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Félicitations ! {kwargs['name']} est né(e) !")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"\nNom de famille : {self.last_name}")
        for member in self.members:
            print(member)


def create_member():
    name = input("Nom : ")
    age = int(input("Âge : "))
    gender = input("Genre (Male/Female) : ")
    is_child_input = input("Est-ce un enfant ? (oui/non) : ").lower()
    is_child = True if is_child_input == "oui" else False
    return {"name": name, "age": age, "gender": gender, "is_child": is_child}


last_name = input("Entrez le nom de famille : ")
my_family = Family(last_name)

num = int(input("Combien de membres voulez-vous ajouter ? "))
for i in range(num):
    print(f"\nCréation du membre #{i+1}")
    member = create_member()
    my_family.add_member(member)


while True:
    print("\n--- Menu ---")
    print("1 - Ajouter un nouvel enfant")
    print("2 - Vérifier si un membre a plus de 18 ans")
    print("3 - Afficher les infos de la famille")
    print("0 - Quitter")
    choice = input("Choisissez une option : ")

    if choice == "1":
        print("\nCréation d'un nouvel enfant :")
        name = input("Nom de l'enfant : ")
        age = int(input("Âge : "))
        gender = input("Genre (Male/Female) : ")
        my_family.born(name=name, age=age, gender=gender, is_child=True)

    elif choice == "2":
        name = input("Nom du membre à vérifier : ")
        if my_family.is_18(name):
            print(f"{name} a 18 ans ou plus.")
        else:
            print(f"{name} a moins de 18 ans.")

    elif choice == "3":
        my_family.family_presentation()

    elif choice == "0":
        print("Au revoir !")
        break

    else:
        print("Option invalide. Réessayez.")
