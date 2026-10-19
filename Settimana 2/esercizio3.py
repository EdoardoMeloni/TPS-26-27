tutti_voti = [5, 7, 8, 4, 2, 8, 9, 6]

def sufficienze (tutti_voti):
    return [voto for voto in tutti_voti if voto >=6]

print (sufficienze(tutti_voti))