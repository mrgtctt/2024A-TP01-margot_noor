# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

water_quantity =float(input("Quelle quantité d'eau faut-il assainir ? "))
Filtre=water_quantity/5
Lampe_UV=3*water_quantity/5
Chlore=water_quantity/10

print(f"Voici les éléments requis pour assainir de {water_quantity}L d'eau : ")
print(f"- Filtre(s) : {Filtre} ")
print(f"- Lampe(s): {Lampe_UV} UV")
print(f"- Chlore : {Chlore}kg")