# TODO: Créer un script permettant le formattage du livre des records des JO.

country = input("De quelle nationalité est l'athlète ? \n")
athlete = input("Quel est le nom de l'athlète ? \n")
date = input("Quelle est la date du record ? \n")
discipline = input("Quelle est la discipline du record ? \n")
catégorie = input("Quelle est la catégorie du record ? \n")
record = input("Quel est le record ? \n")

if catégorie: 
    print("Nouveau Record : ")
    print("--------------------")
    print(f"{date} - {discipline} - {catégorie}:")
    print(f"    {athlete} {country} - {record}")
else : 
    print("Nouveau Record : ")
    print("--------------------")
    print(f"{date} - {discipline}")
    print(f"{athlete} {country} - {record}")
