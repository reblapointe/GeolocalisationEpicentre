
class Point:
    def __init__(self, descriptif:str = "origine", x:float = 0, y:float = 0):
        self.descriptif = descriptif
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.descriptif} ({self.x}, {self.y})"

    
