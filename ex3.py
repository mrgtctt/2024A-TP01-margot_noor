# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.
import math 
speed = float(input("Vitesse initiale (m/s): ")) 
angle = float(input("Angle de lancer (en degrés): "))
angle_rad = math.radians(angle)
x = ((speed)**2 * math.sin(2*angle_rad) )/9.80
phrase = "Distance parcourue: {}m".format(round(x,2))
print(phrase)