# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

water_quantity =float(input("Veuillez saisir la quantité à assainir:\n"))
Filtre=water_quantity/5
Lampe_UV=3*water_quantity/5
Chlore=water_quantity/10
print("Voici les matériaux requis pour l'assainissement de", water_quantity," L d'eau\n" "",Filtre,"filtres\n" "", Lampe_UV,"lampes UV\n" "", Chlore, "kg de chlore")

print(f"Voici les matériaux requis pour l'assainissement de {water_quantity}L d'eau : ")
print(f"- {filtre} filtres")
print(f"- {uv} lampes UV")
print(f"- {chlore}kg de chlore")