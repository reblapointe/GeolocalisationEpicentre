
class Point:
    '''Un point nommé dans le plan'''
    def __init__(self, nom:str = "origine", x:float = 0, y:float = 0):
        self.nom = nom
        self.x = x
        self.y = y

    def description(self):
        '''Retourne une description textuelle du point'''
        return f"{self.nom} ({self.x}, {self.y})"

    
