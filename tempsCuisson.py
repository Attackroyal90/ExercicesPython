"Saisie des caracteristiques de la viande par l'utilisateur"
type_viande = input("Choisissez le type de viande entre le boeuf, le canard et le porc : ")
poids_viande = float(input("Choisissez le poids de votre viande en grammes : "))
mode_cuisson = input("Choisissez le mode de cuisson entre une cuisson bleu (rose pour le canard), a point et bien cuit : ")

"Affichage de l'ensemble des choix"
print("Vous avez donc choisi une viande de",type_viande,", qui pèse",poids_viande,"g, et avec une cuisson",mode_cuisson)

"""Méthode de calcul de la duree de cuisson du boeuf en fonction du
mode de cuisson et du poids"""
def cuisson_boeuf() :
    global temps_coeff
    if mode_cuisson == "bleu" :
        temps_coeff = 0.02
    elif mode_cuisson == "a point" :
        temps_coeff = 0.034
    elif mode_cuisson == "bien cuit" :
        temps_coeff = 0.05
    return temps_coeff * poids_viande

"""Méthode de calcul de la duree de cuisson du porc en fonction du
mode de cuisson et du poids"""
def cuisson_porc() :
    global temps_coeff
    if mode_cuisson == "bleu" :
        temps_coeff = 0.0375
    elif mode_cuisson == "a point" :
        temps_coeff = 0.0625
    elif mode_cuisson == "bien cuit" :
        temps_coeff = 0.1
    return temps_coeff * poids_viande

"""Méthode de calcul de la duree de cuisson du canard en fonction du
mode de cuisson et du poids"""
def cuisson_canard() :
    global temps_coeff
    if mode_cuisson == "rose" :
        temps_coeff = 0.04444
    elif mode_cuisson == "a point" :
        temps_coeff = 0.05555
    elif mode_cuisson == "bien cuit" :
        temps_coeff = 0.06666
    return temps_coeff * poids_viande

"""Affichage du temps de cuisson de la viande à l'aide de 
la methode appropriee"""
if type_viande == "boeuf" :
    print("Le temps de cuisson de ce morceau de boeuf de",poids_viande,"g  de",cuisson_boeuf()," min")
elif type_viande == "canard" :
    print("Le temps de cuisson de ce morceau de canard de",poids_viande,"g  de",cuisson_canard()," min")
elif type_viande == "porc" :
    print("Le temps de cuisson de ce morceau de porc de",poids_viande,"g sera de",cuisson_porc()," min")