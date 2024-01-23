'''
Permet de géolocaliser l'épicentre d'un tremblement de terre à partir de la distance
qui le sépare de trois points (Jonquière, Roberval et Dolbeau)
'''

from triangle import Triangle
from point import Point


jonquiere = Point("Jonquiere", 100, 0)
roberval = Point("Roberval", 0, 0)
dolbeau = Point("Dolbeau", 200, 200)

sag_lac = Triangle(jonquiere, roberval, dolbeau)

print(f"Entrez la distance à {sag_lac.point_a.nom}")
d1 = int(input())

print(f"Entrez la distance à {sag_lac.point_b.nom}")
d2 = int(input())

print(f"Entrez la distance à {sag_lac.point_c.nom}")
d3 = int(input())

epicentre = sag_lac.trianguler(d1, d2, d3)
print(epicentre.description())
print(sag_lac.description())

arvida = jonquiere
arvida.nom = 'arvida' #jonquiere.nom a-t-il changé?
