from triangle import Triangle
from point import Point

desArpenteurs = Triangle(Point("Jonquiere", 100, 0), Point("Alma", 0, 0), Point("Dolbeau", 200, 200))

print(f"Entrez la distance à {desArpenteurs.point_a.descriptif}")
d1 = int(input())

print(f"Entrez la distance à {desArpenteurs.point_b.descriptif}")
d2 = int(input())

print(f"Entrez la distance à {desArpenteurs.point_c.descriptif}")
d3 = int(input())

epicentre = desArpenteurs.trianguler(d1, d2, d3)
print(epicentre)
print(desArpenteurs)