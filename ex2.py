# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

water_quantity =float(input("Quelle quantité d'eau faut-il assainir ? "))
Filtre=int(water_quantity/5)
Lampe_UV=int(3*water_quantity/5)
Chlore=float(water_quantity/10)
print(f"""Voici les éléments requis pour assainir {water_quantity}L d'eau:
\t- Filtre(s) : {Filtre}
\t- Lampe(s) UV : {Lampe_UV}
\t- Chlore : {Chlore}kg""")

#print(f"Voici les éléments requis pour assainir {water_quantity}L d'eau: ")
#print(f"- Filtre(s) : {Filtre} ")
#print(f"- Lampe(s): {Lampe_UV} UV")
#print(f"- Chlore : {Chlore}kg")