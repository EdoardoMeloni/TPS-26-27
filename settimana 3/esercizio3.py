def parola_piu_lunga(nome_file):
    migliore = ""
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            for parola in riga.split():
                pulita = parola.strip(".,;:!?«»'\"")
                if len(pulita) > len(migliore):
                    migliore = pulita
    return migliore

p = parola_piu_lunga("dati/commedia.txt")
print(p, "-", len(p), "lettere")