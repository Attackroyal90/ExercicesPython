print("Le prix du café est de 0.60€")
print("Les pièces acceptées : 2€ 1€ 0.50€ 0.20€ 0.10€ 0.05€")
montant_paye = 0.0

"Recupere l'argent pour le cafe avec seulement des pieces valides"
while montant_paye < 0.6 :
    paiement = float(input("Saisissez la valeur du montant de votre pièce :"))
    if paiement == 2 or paiement == 1 or paiement == 0.5 or paiement == 0.2 or paiement == 0.1 or paiement == 0.05 :
        montant_paye += paiement
        print("Montant paye :",montant_paye,"€ sur 0.6€")
    else:
        print("La valeur de la pièce est incorrecte, veuillez réessayer")

"Rend la monnaie en pieces valides"
if montant_paye > 0.6 :
    monnaie_brute = montant_paye - 0.6
    monnaie  = round(monnaie_brute, 2)
    print("Voici votre monnaie :",monnaie)
    while monnaie > 0.05 :
        if monnaie >= 2 :
            print("Une piece de deux euros")
            monnaie -= 2
        while monnaie >= 1 :
            print("Une piece de un euro")
            monnaie -= 1
        while monnaie >= 0.5 :
            print("Une piece de cinquantes centimes")
            monnaie -= 0.5
        while monnaie >= 0.2 :
            print("Une piece de vingts centimes")
            monnaie -= 0.2
        while monnaie >= 0.1 :
            print("Une piece de dix centimes")
            monnaie -= 0.1
        while monnaie >= 0.05 :
            print("Une piece de cinq centimes")
            monnaie -= 0.05
else :
    print("Pas de monnaie à rendre")
print("Fin de la transaction")