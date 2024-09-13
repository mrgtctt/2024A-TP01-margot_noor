# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.
import math 
speed = float(input("Veuillez saisir la vitesse intiale de la boule ? \n")) 
angle = float(input("Veuillez saisir l'angle inital en degré ? \n"))
angle_rad = math.radians(angle)
x = ((speed)**2 * math.sin(2*angle_rad) )/9.80
phrase = "La distance maximale en x est de {} m.".format(round(x,2))
print(phrase)