#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country =input("Pays concerné ? ")
code_medals =str(input("Chaine représentant les médailles ? "))
valid_caracter=("G","B","S")
ore,argent,bronze=0,0,0
if set(code_medals).issubset(valid_caracter):
  for i in range(0,len(code_medals)) :
    if code_medals[i]==("G"):
       ore=ore+1
    if code_medals[i]==("S"):
       argent=argent+1
    if code_medals[i]==("B"):
       bronze=bronze+1

  print(f"{country}:\n- {ore} Or\n- {argent} Argent\n- {bronze} Bronze")
  #f" -{ore} Or\n -{argent} Argent\n -{bronze} Bronze")
else:
   print("Ceci est une chaine invalide.")

