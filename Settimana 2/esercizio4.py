lista = ["Sara", "Luca", "Sara", "Marco", "Luca", "Giulia"]

def senza_duplicati(lista):
    listan = []
    for nome in lista:
        attuale = nome
        for nome in lista:
            if attuale in lista and attuale not in listan:
                listan.append(attuale)
    return (listan)


print (senza_duplicati(lista))