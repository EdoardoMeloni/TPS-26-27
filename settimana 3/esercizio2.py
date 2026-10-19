def conta_righe(nome_file):
    totali = 0
    piene = 0
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            totali += 1
            if riga.strip() != "":
                piene += 1
    return totali, piene

for nome in ["dati/parole.txt", "dati/commedia.txt"]:
    tot, piene = conta_righe(nome)
    print(f"{nome}: {tot} righe, {piene} non vuote")