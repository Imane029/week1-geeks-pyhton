def display_board(board):
    """Affiche le plateau de jeu"""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def player_input(player, board):
    """Demande au joueur de choisir une case valide"""
    while True:
        try:
            position = int(input(f"Joueur {player}, choisissez une case (1-9): ")) - 1
            if position < 0 or position > 8:
                print("❌ Position invalide, choisissez entre 1 et 9.")
            elif board[position] != " ":
                print("❌ Case déjà occupée, choisissez une autre.")
            else:
                return position
        except ValueError:
            print("❌ Entrez un nombre valide (1-9).")


def check_win(board, mark):
    """Vérifie si le joueur a gagné"""
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]             
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == mark:
            return True
    return False


def is_board_full(board):
    """Vérifie si le plateau est plein"""
    return " " not in board


def play():
    """Fonction principale pour jouer au Tic Tac Toe"""
    board = [" "] * 9  
    current_player = "X"
    
    print("Bienvenue au jeu Tic Tac Toe !")
    display_board(board)
    
    while True:
        position = player_input(current_player, board)
        board[position] = current_player
        display_board(board)
        
        if check_win(board, current_player):
            print(f"🎉 Joueur {current_player} a gagné !")
            break
        elif is_board_full(board):
            print("😐 Match nul !")
            break
        
        
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play()
