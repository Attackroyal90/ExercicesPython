def recup_infos():
    # Demande du texte chiffre et de la cle
    texte = input("Saisissez le texte chiffré :")
    decalage = int(input("Saisissez le décalage :"))

    # Tout en majuscule pour eviter les conflits
    texte = texte.upper()

    texte_avec_cle = list(texte)
    texte_decrypte = ''

    return texte,decalage,texte_decrypte,texte_avec_cle;

def decryptage_cesar():
    texte,decalage,texte_decrypte,texte_avec_cle = recup_infos()
    #Decryptage lettre par lettre
    a = 0
    for i in range(len(texte)):

        #Si lettre, on decrypte
        if texte[i].isalpha():

            #On déchiffre la lettre
            lettre_decrypte = (ord(texte[i]) -65 - decalage + 26) % 26
            texte_decrypte += chr(lettre_decrypte + 65)

        #Pas de lettre, on laisse comme c'est
        else:
            texte_decrypte += texte[i]

    print(texte_decrypte)