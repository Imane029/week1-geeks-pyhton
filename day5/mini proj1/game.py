import random

class Game:
    def __init__(self):
        self.items = ["rock", "paper", "scissors"]

    def get_user_item(self):
        """Demande à l'utilisateur un choix valide"""
        while True:
            choice = input("Choisissez rock, paper ou scissors: ").lower()
            if choice in self.items:
                return choice
            print("❌ Choix invalide. Réessayez.")

    def get_computer_item(self):
        """Retourne un choix aléatoire de l'ordinateur"""
        return random.choice(self.items)

    def get_game_result(self, user_item, computer_item):
        """Détermine le résultat du jeu"""
        if user_item == computer_item:
            return "draw"
        elif (
            (user_item == "rock" and computer_item == "scissors") or
            (user_item == "paper" and computer_item == "rock") or
            (user_item == "scissors" and computer_item == "paper")
        ):
            return "win"
        else:
            return "loss"

    def play(self):
        """Lance une partie complète"""
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"\n👉 Vous avez choisi {user_item}.")
        print(f"💻 L'ordinateur a choisi {computer_item}.")

        if result == "win":
            print("🎉 Vous avez gagné !")
        elif result == "loss":
            print("😢 Vous avez perdu.")
        else:
            print("😐 Égalité.")

        return result
