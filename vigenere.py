def repeat_key(key, length):
    """Répète la clé pour correspondre à la longueur du message"""
    return (key * ((length // len(key)) + 1))[:length]


def vigenere_decrypt(ciphertext, key):
    """Déchiffre un texte chiffré avec Vigenère et une clé donnée"""
    plaintext = ""
    key = key.upper()
    key_index = 0  # Position dans la clé répétée

    for char in ciphertext:
        if char.isalpha():
            # On travaille sur des majuscules ou minuscules séparément
            is_upper = char.isupper()
            offset = ord('A') if is_upper else ord('a')

            # Lettre clé actuelle (toujours en majuscule)
            k = ord(key[key_index % len(key)]) - ord('A')
            c = ord(char) - offset

            # Déchiffrement : (C - K + 26) % 26
            p = (c - k + 26) % 26
            decrypted_char = chr(p + offset)

            plaintext += decrypted_char
            key_index += 1  # On n’avance la clé que si on a traité une lettre
        else:
            # On conserve les espaces, ponctuations, etc.
            plaintext += char

    return plaintext


def main():
    ciphertext = """Gqfltwj emgj clgfv ! Aqltj rjqhjsksg ekxuaqs, ua xtwk
n'feuguvwb gkwp xwj, ujts f'npxkqvjgw nw tjuwcz
ugwygjtfkf qz uw efezg sqk gspwonu. Jgsfwb-aqmu f
Pspygk nj 29 cntnn hqzt dg igtwy fw xtvjg rkkunqf."""

    key = "FCSC"
    decrypted = vigenere_decrypt(ciphertext, key)
    print("=== Message déchiffré ===")
    print(decrypted)


if __name__ == "__main__":
    main()