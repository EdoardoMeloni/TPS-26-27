def salva_appunto(testo):
    with open("appunti.txt", "a", encoding="utf-8") as f:
        f.write(testo + "\n")

salva_appunto("comprare il libro")
salva_appunto("ripassare i file")
salva_appunto("consegnare su GitHub")

with open("appunti.txt", "r", encoding="utf-8") as f:
    for numero, riga in enumerate(f, start=1):
        print(numero, riga.strip())