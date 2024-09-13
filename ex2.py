# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

water_quantity = float(input("Veuillez saisir la quantité d'eau à assainir(en L) \n"))
filtre = water_quantity / 5 
uv = water_quantity * 0.60
chlore = water_quantity * 0.1 

print(f"Voici les matériaux requis pour l'assainissement de {water_quantity}L d'eau : ")
print(f"- {filtre} filtres")
print(f"- {uv} lampes UV")
print(f"- {chlore}kg de chlore")