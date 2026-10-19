def conta_unici(lista):
    return  len(set(lista))

persone = ["luca", "edoardo", "pietro"]

print(conta_unici(persone))

persone = ["luca", "edoardo", "pietro", "marco"]

print(conta_unici(persone))
