import time
import copy

class GameOfLife:
    def __init__(self, rows, cols, initial_state=None):
        """
        rows, cols : dimensions de la grille
        initial_state : liste de tuples (x, y) pour les cellules vivantes
        """
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        
        if initial_state:
            for x, y in initial_state:
                if 0 <= x < rows and 0 <= y < cols:
                    self.grid[x][y] = 1

    def display(self):
        """Affiche la grille"""
        for row in self.grid:
            line = "".join(['█' if cell else ' ' for cell in row])
            print(line)
        print("\n" + "-"*self.cols)

    def count_live_neighbors(self, x, y):
        """Compte les voisins vivants autour de la cellule (x, y)"""
        count = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if (i == x and j == y) or i < 0 or j < 0 or i >= self.rows or j >= self.cols:
                    continue
                count += self.grid[i][j]
        return count

    def next_generation(self):
        """Calcule la prochaine génération"""
        new_grid = copy.deepcopy(self.grid)
        for i in range(self.rows):
            for j in range(self.cols):
                live_neighbors = self.count_live_neighbors(i, j)
                if self.grid[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_grid[i][j] = 0  
                else:
                    if live_neighbors == 3:
                        new_grid[i][j] = 1  
        self.grid = new_grid


if __name__ == "__main__":
   
    initial_state = [(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
    game = GameOfLife(rows=10, cols=10, initial_state=initial_state)

    generations = 20 
    for gen in range(generations):
        print(f"Génération {gen+1}")
        game.display()
        game.next_generation()
        time.sleep(0.5)
