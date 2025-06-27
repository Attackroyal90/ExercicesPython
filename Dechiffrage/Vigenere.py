def recup_infos():
    # Demande du texte chiffre et de la cle
    texte = input("Saisissez le texte chiffré :")
    key = input("Saisissez la clé :")

    # Tout en majuscule pour eviter les conflits
    texte = texte.upper()
    key = key.upper()

    texte_avec_cle = list(texte)
    lettre = list(key)
    texte_decrypte = ''

    return texte,key,texte_decrypte,lettre,texte_avec_cle;

def decryptage_vigenere():
    texte,key,texte_decrypte,lettre,texte_avec_cle = recup_infos()
    #Decryptage lettre par lettre
    a = 0
    for i in range(len(texte)):
        #Si lettre, on decrypte
        if texte[i].isalpha():
            #Boucle pour que la cle se relance jusqu'a la fin du texte
            texte_avec_cle[i] = lettre[a]
            a += 1
            if a == len(key):
                a = 0

            #On déchiffre la lettre
            lettre_decrypte = (ord(texte[i]) - ord(texte_avec_cle[i]) + 26) % 26
            texte_decrypte += chr(lettre_decrypte + 65)

        #Pas de lettre, on laisse comme c'est
        else:
            texte_decrypte += texte[i]

    print(texte_decrypte)