# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100])
battery_level =float(input("Pourcentage de batterie ? "))
Distance,Distance_1,Distance_2,Distance_3,Distance_4,Distance_5=0,0,0,0,0,0

if battery_level==0:
    print("La batterie est vide")
else:
    if battery_level>50:
        Distance=(battery_level-50)*2
        battery_level=50
    if battery_level>25:
        Distance_1=((battery_level-25)*0.5)
        battery_level=25
    if battery_level>10:
        Distance_2= ((battery_level-10)*1)
        battery_level=10
    if battery_level>5:
        Distance_3=((battery_level-5)*2.5)
        battery_level=5
    if battery_level>0:
        Distance_4= (battery_level)*6
    Distance_5=round(Distance+Distance_1+Distance_2+Distance_3+Distance_4,1)
    print(Distance_5,"km")

   





