# TODO: Créer un script permettant le formattage du livre des records des JO.

country = input("De quelle nationalité est l'athlète ? ")
athlete = input("Quel est son nom ? ")
date = input("Date du record ? ")
sport = input("Dans quelle discipline ? ")
category = input("Dans une catégorie spécifique ? ")
record = input("Quel est le record ? ")
print( f"\nNouveau Record:\n--------------------\n{date} - {sport} - {category}:\n\t{athlete} ({country}) - {record}")

#if catégorie: 
 #   print("Nouveau Record : ")
  #  print("--------------------")
   # print(f"{date} - {discipline} - {catégorie}:")
    #print(f"    {athlete} {country} - {record}")
#else : 
 #   print("Nouveau Record : ")
  #  print("--------------------")
   # print(f"{date} - {discipline}")
    #print(f"{athlete} {country} - {record}")
