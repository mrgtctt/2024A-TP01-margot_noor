#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country = input("Quel est le pays concerné ? \n")
code_medals = str(input("Veuillez entrer les résultats ? \n"))
l = len(code_medals)
nbr_g = code_medals.count("G")
nbr_s = code_medals.count("S")
nbr_b = code_medals.count("B")
nbr_tot = nbr_g + nbr_s + nbr_b 
if l == nbr_tot : 
    print("Medailles : ")
    print(f"- {nbr_g} Or")
    print(f"- {nbr_s} Argent")
    print(f"- {nbr_b} Bronze")
else : 
    print("Veuillez saisir une chaîne valide.")
