dizionario = {"Italia": "Roma", "Francia": "Parigi", "Spagna": "Madrid"}

def capitale(paese):
    return dizionario.get(paese, "non in elenco")

print (capitale("Italia"))
print (capitale("Marocco"))