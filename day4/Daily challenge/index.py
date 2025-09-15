import math

class Pagination:
    def __init__(self, items=None, page_size=10):
        
        self.items = items if items is not None else []
        self.page_size = page_size
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    def get_visible_items(self):
        """Retourne les éléments visibles sur la page courante"""
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

   
    def go_to_page(self, page_num):
        """Navigue vers la page spécifiée (1-based)"""
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(f"Page {page_num} hors limites. Pages disponibles : 1-{self.total_pages}")
        self.current_idx = page_num - 1
        return self  

    def first_page(self):
        """Navigue à la première page"""
        self.current_idx = 0
        return self

    def last_page(self):
        """Navigue à la dernière page"""
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        """Passe à la page suivante si possible"""
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        """Retourne à la page précédente si possible"""
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    
    def __str__(self):
        """Affiche les éléments de la page courante, un par ligne"""
        return "\n".join(str(item) for item in self.get_visible_items())


# Exemple d'utilisation
if __name__ == "__main__":
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")
    p = Pagination(alphabetList, 4)

    print("Page actuelle :", p.get_visible_items()) 
    p.next_page()
    print("Page suivante :", p.get_visible_items())  
    p.last_page()
    print("Dernière page :", p.get_visible_items())  
    
    try:
        p.go_to_page(10)
    except ValueError as e:
        print("Erreur :", e)
    
    p.go_to_page(7)
    print("Page 7 index interne :", p.current_idx + 1)  # 7

    try:
        p.go_to_page(0)  
    except ValueError as e:
        print("Erreur :", e)

    
    print("\nAffichage page courante avec __str__():")
    print(p)
