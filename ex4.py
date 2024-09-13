# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level = int(input("Veuillez saisir le pourcentage de batterie du bateau\n"))
distance, distance_1, distance_2, distance_3, distance_4, distance_5 = 0, 0, 0, 0, 0, 0

if battery_level < 0 or battery_level > 100 : 
    print("Veuillez saisir une valeur comprise entre 0 et 100")

else :
    if battery_level > 50 or battery_level <= 100 :
        distance_1 = (battery_level - 50)*2 
        battery_level = 50

    if battery_level > 25 or battery_level<= 50 : 
        distance_2 = (battery_level - 25 )*0.5 
        battery_level = 25

    if battery_level > 10 or battery_level <=25 :
        distance_3 = (battery_level - 10)*1 
        battery_level = 10

    if battery_level > 5 or battery_level <= 10 : 
        distance_4 = (battery_level - 5)*2.5 
        battery_level = 5

    if battery_level > 0 or battery_level <= 5: 
        distance_5 = (battery_level)*6
    
    if battery_level == 0 :
        print("La distance possible est de 0 km")

    distance = distance_1 + distance_2 + distance_3 + distance_4 + distance_5

    print("La distance possible est de {}km.".format(round(distance,1)))

