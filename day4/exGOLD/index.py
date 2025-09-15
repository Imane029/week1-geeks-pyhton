

class BankAccount:
    def __init__(self, balance=0, username="", password=""):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = False

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
            print(f"Utilisateur {username} authentifié avec succès.")
        else:
            raise Exception("Échec de l'authentification!")

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("Veuillez vous authentifier d'abord!")
        if amount <= 0:
            raise Exception("Le montant du dépôt doit être positif!")
        self.balance += amount
        print(f"Dépôt de {amount} effectué. Nouveau solde: {self.balance}")

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Veuillez vous authentifier d'abord!")
        if amount <= 0:
            raise Exception("Le montant du retrait doit être positif!")
        if amount > self.balance:
            raise Exception("Solde insuffisant!")
        self.balance -= amount
        print(f"Retrait de {amount} effectué. Nouveau solde: {self.balance}")


class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance=0, username="", password="", minimum_balance=0):
        super().__init__(balance, username, password)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Veuillez vous authentifier d'abord!")
        if amount <= 0:
            raise Exception("Le montant du retrait doit être positif!")
        if self.balance - amount < self.minimum_balance:
            raise Exception(f"Impossible de retirer. Le solde minimum de {self.minimum_balance} doit être maintenu.")
        self.balance -= amount
        print(f"Retrait de {amount} effectué. Nouveau solde: {self.balance}")


class ATM:
    def __init__(self, account_list, try_limit=2):
        if not isinstance(account_list, list) or not all(isinstance(a, BankAccount) for a in account_list):
            raise Exception("account_list doit contenir uniquement des instances de BankAccount ou MinimumBalanceAccount.")
        if try_limit <= 0:
            print("try_limit invalide, il sera défini à 2.")
            try_limit = 2

        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0

        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("\n=== Menu Principal ATM ===")
            print("1. Se connecter")
            print("2. Quitter")
            choice = input("Choisir une option: ")

            if choice == "1":
                username = input("Nom d'utilisateur: ")
                password = input("Mot de passe: ")
                self.log_in(username, password)
            elif choice == "2":
                print("Au revoir!")
                break
            else:
                print("Option invalide. Réessayez.")

    def log_in(self, username, password):
        for account in self.account_list:
            try:
                account.authenticate(username, password)
                self.show_account_menu(account)
                return
            except:
                continue

        self.current_tries += 1
        print(f"Échec de l'authentification. Tentative {self.current_tries}/{self.try_limit}")
        if self.current_tries >= self.try_limit:
            print("Nombre maximum de tentatives atteint. ATM éteint.")
            exit()

    def show_account_menu(self, account):
        while True:
            print(f"\n--- Menu Compte ({account.username}) ---")
            print("1. Déposer")
            print("2. Retirer")
            print("3. Quitter")
            choice = input("Choisir une option: ")

            if choice == "1":
                try:
                    amount = float(input("Montant à déposer: "))
                    account.deposit(amount)
                except Exception as e:
                    print(e)
            elif choice == "2":
                try:
                    amount = float(input("Montant à retirer: "))
                    account.withdraw(amount)
                except Exception as e:
                    print(e)
            elif choice == "3":
                print("Déconnexion...")
                account.authenticated = False
                break
            else:
                print("Option invalide. Réessayez.")



if __name__ == "__main__":
    acc1 = BankAccount(balance=1000, username="user1", password="pass1")
    acc2 = MinimumBalanceAccount(balance=500, username="user2", password="pass2", minimum_balance=100)

    atm = ATM(account_list=[acc1, acc2], try_limit=3)
