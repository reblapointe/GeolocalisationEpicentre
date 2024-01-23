import math 
from point import Point


class Triangle:
    
    PRECISION = 0.001   

    def __init__(self, point_a:Point, point_b:Point, point_c:Point):
        if (Triangle.est_valide(point_a, point_b, point_c)):
            self.point_a = point_a
            self.point_b = point_b
            self.point_c = point_c
        else:
            raise ValueError("Les points fournis ne forment pas un triangle")

    def cote_ab(self):
        return math.sqrt(
            (self.point_a.x - self.point_b.x)**2 + 
            (self.point_a.y - self.point_b.y)**2)
    
    def cote_bc(self):
        return math.sqrt(
            (self.point_b.x - self.point_c.x)**2 + 
            (self.point_b.y - self.point_c.y)**2)
    
    def cote_ca(self):
        return math.sqrt(
            (self.point_c.x - self.point_a.x)**2 + 
            (self.point_c.y - self.point_a.y)**2)

    def est_valide(point_a, point_b, point_c):

        cote_ab = math.sqrt((point_a.x - point_b.x)**2 + (point_a.y - point_b.y)**2)
        cote_bc = math.sqrt((point_b.x - point_c.x)**2 + (point_b.y - point_c.y)**2)
        cote_ca = math.sqrt((point_c.x - point_a.x)**2 + (point_c.y - point_a.y)**2)
    
        cote_ab_valide = cote_ab > Triangle.PRECISION and cote_ab < cote_bc + cote_ca - Triangle.PRECISION
        cote_bc_valide = cote_bc > Triangle.PRECISION and cote_bc < cote_ca + cote_ab - Triangle.PRECISION
        cote_ca_valide = cote_ca > Triangle.PRECISION and cote_ca < cote_ab + cote_bc - Triangle.PRECISION

        return cote_ab_valide and cote_bc_valide and cote_ca_valide
    
    def perimetre(self) -> float:
        return self.cote_ab() + self.cote_bc() + self.cote_ca()
    
    def aire(self) -> float:
        p = self.perimetre() / 2
        return math.sqrt(p * (p - self.cote_ab()) * (p - self.cote_bc()) * (p - self.cote_ca()))
    
    def a_peu_pres(x:float, y:float) -> bool:
        return x > y - Triangle.PRECISION and x < y + Triangle.PRECISION
    
    def est_equilateral(self) -> bool:
        return Triangle.a_peu_pres(self.cote_ab(), self.cote_bc()) and Triangle.a_peu_pres(self.cote_ab(), self.cote_ca())
    
    def est_isocele(self) -> bool:
        return (Triangle.a_peu_pres(self.cote_ab(), self.cote_bc()) 
                or Triangle.a_peu_pres(self.cote_ab(), self.cote_ca()) 
                or Triangle.a_peu_pres(self.cote_bc(), self.cote_ca()))
    
    def est_rectangle(self) -> bool:
        return (Triangle.a_peu_pres(self.angle_a(), math.pi / 2) 
                or Triangle.a_peu_pres(self.angle_b(), math.pi / 2) 
                or Triangle.a_peu_pres(self.angle_c(), math.pi / 2))
    
    def est_scalene(self) -> bool:
        return not self.est_isocele(self)

    def angle_a(self) -> float:
         return math.acos(
             (self.cote_ab()**2 - self.cote_bc()**2 + self.cote_ca()**2) / (2 * self.cote_ca() * self.cote_ab()))
    
    def angle_b(self) -> float:
         return math.acos((self.cote_ab() ** 2 + self.cote_bc() ** 2 - self.cote_ca() ** 2) / (2 * self.cote_ab() * self.cote_bc()))
    
    def angle_c(self) -> float:
         return math.acos((-self.cote_ab() ** 2 + self.cote_bc() ** 2 + self.cote_ca() ** 2) / (2 * self.cote_bc() * self.cote_ca()))
    
    def trianguler(self, distance_a:float, distance_b:float, distance_c:float, descriptif="Épicentre") -> Point:
        A = 2 * self.point_b.x - 2 * self.point_a.x
        B = 2 * self.point_b.y - 2 * self.point_a.y
        C = distance_a**2 - distance_b**2 - self.point_a.x**2 + self.point_b.x**2 - self.point_a.y**2 + self.point_b.y**2
        D = 2 * self.point_c.x - 2 * self.point_b.x
        E = 2 * self.point_c.y - 2 * self.point_b.y
        F = distance_b**2 - distance_c**2 - self.point_b.x**2 + self.point_c.x**2 - self.point_b.y**2 + self.point_c.y**2
        x = (C * E - F * B) / (E * A - B * D)
        y = (C * D - A * F) / (B * D - A * E)
        return Point(descriptif, x, y)

    def __str__(self):
        return  (
            f"Le triangle formé de {self.point_a.descriptif}, {self.point_b.descriptif} et {self.point_c.descriptif} a les caractéristiques suivantes : \n" +
            f"{self.point_a}, {self.point_b},  {self.point_c}\n" +
            f"{self.point_a.descriptif}-{self.point_b.descriptif} = {round(self.cote_ab(), 2)}, " +
            f"{self.point_b.descriptif}-{self.point_c.descriptif} = {round(self.cote_bc(), 2)}, " +
            f"{self.point_c.descriptif}-{self.point_a.descriptif} = {round(self.cote_ca(), 2)}\n" +
            f"Angle à {self.point_a.descriptif} = {round(self.angle_a(), 2)} ({round(math.degrees(self.angle_a()), 2)}°)\n" +
            f"Angle à {self.point_b.descriptif} = {round(self.angle_b(), 2)} ({round(math.degrees(self.angle_b()), 2)}°)\n" +
            f"Angle à {self.point_c.descriptif} = {round(self.angle_c(), 2)} ({round(math.degrees(self.angle_c()), 2)}°)\n" +
            f"Aire = {round(self.aire(), 2)}\n" +
            f"Périmetre = {round(self.perimetre(), 2)}\n" +
            f"Ce triangle est {'équilatéral' if self.est_equilateral() else 'isocèle' if self.est_isocele() else 'scalène'}" +
            f"{' rectangle' if self.est_rectangle() else ''}.\n")
