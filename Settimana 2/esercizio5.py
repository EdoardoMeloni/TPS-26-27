def conta_parole(frase):
    conteggio = {}
    for parola in frase.lower().split():
        conteggio[parola] = conteggio.get(parola, 0) + 1
    return conteggio

frase = "il gatto corre insieme al topo ed al cane in giro per la citta"
risultato = conta_parole(frase)
print(risultato)

piu_frequente = max(risultato, key=risultato.get)
print(piu_frequente, risultato[piu_frequente])