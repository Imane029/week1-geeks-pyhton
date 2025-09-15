from game import Game

def get_user_menu_choice():
    """Affiche le menu et retourne le choix de l'utilisateur"""
    print("\n=== Menu ===")
    print("1. Jouer une nouvelle partie")
    print("2. Voir les scores")
    print("x. Quitter")
    choice = input("Votre choix: ").lower()

    if choice in ["1", "2", "x"]:
        return choice
    else:
        print("❌ Choix invalide, réessayez.")
        return None


def print_results(results):
    """Affiche les résultats finaux"""
    print("\n=== Résultats finaux ===")
    print(f"Victoires : {results['win']}")
    print(f"Défaites : {results['loss']}")
    print(f"Égalités : {results['draw']}")
    print("\nMerci d'avoir joué ! 👋")


def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()
        if not choice:
            continue  

        if choice == "1":  
            game = Game()
            result = game.play()
            results[result] += 1

        elif choice == "2":  
            print_results(results)

        elif choice == "x":  
            print_results(results)
            break


if __name__ == "__main__":
    main()
