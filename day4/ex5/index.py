
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


class TheIncredibles(Family):
    def __init__(self, last_name):
        super().__init__(last_name)

    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{member['name']} utilise son pouvoir : {member['power']} !")
                else:
                    raise Exception(f"{member['name']} n'a pas plus de 18 ans, impossible d'utiliser le pouvoir.")

    def incredible_presentation(self):
        print("\n*** Voici notre famille incroyable ***")
        super().family_presentation()


def create_incredible_member():
    name = input("Nom : ")
    age = int(input("Âge : "))
    gender = input("Genre (Male/Female) : ")
    power = input("Pouvoir : ")
    incredible_name = input("Nom incroyable : ")
    is_child_input = input("Est-ce un enfant ? (oui/non) : ").lower()
    is_child = True if is_child_input == "oui" else False
    return {
        "name": name,
        "age": age,
        "gender": gender,
        "is_child": is_child,
        "power": power,
        "incredible_name": incredible_name
    }


last_name = input("Entrez le nom de famille : ")
incredible_family = TheIncredibles(last_name)

num = int(input("Combien de membres voulez-vous ajouter ? "))
for i in range(num):
    print(f"\nCréation du membre incroyable #{i+1}")
    member = create_incredible_member()
    incredible_family.add_member(member)


while True:
    print("\n--- Menu ---")
    print("1 - Utiliser le pouvoir d'un membre")
    print("2 - Ajouter un nouvel enfant incroyable")
    print("3 - Afficher la famille incroyable")
    print("0 - Quitter")
    choice = input("Choisissez une option : ")

    if choice == "1":
        name = input("Nom du membre pour utiliser le pouvoir : ")
        try:
            incredible_family.use_power(name)
        except Exception as e:
            print(e)

    elif choice == "2":
        print("\nCréation d'un nouvel enfant incroyable :")
        name = input("Nom : ")
        age = int(input("Âge : "))
        gender = input("Genre (Male/Female) : ")
        power = input("Pouvoir : ")
        incredible_name = input("Nom incroyable : ")
        incredible_family.born(name=name, age=age, gender=gender, is_child=True, power=power, incredible_name=incredible_name)

    elif choice == "3":
        incredible_family.incredible_presentation()

    elif choice == "0":
        print("Au revoir !")
        break

    else:
        print("Option invalide. Réessayez.")
