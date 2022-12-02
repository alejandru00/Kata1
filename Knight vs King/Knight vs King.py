def knight_vs_king (knight_position, king_position):
    distancialetras = knight_position[0] - king_position[0]
    distancianumeros = ord(knight_position[1]) - ord(king_position[1])
    distancia = distancialetras**2 + distancianumeros**2
    if distancia == 5: 
        return 'Knight'
    elif distancia < 3: 
        return 'King'
    else:
        return 'None'