def alphabet_war(fight):
    puntos1 = 0
    puntos2 = 0
    equipo1 = {"w":4,"p":3,"b":2,"s":1}
    equipo2 = {"m":4,"q":3,"d":2,"z":1}
    
    for letra in fight:
        if letra in equipo1:
            puntos1 += equipo1[letra]
        elif letra in equipo2:
            puntos2 += equipo2[letra]
    if puntos1 > puntos2:
        return "Left side wins!"
    elif puntos1 < puntos2:
        return "Right side wins!"
    else:
        return "Let's fight again!"
    