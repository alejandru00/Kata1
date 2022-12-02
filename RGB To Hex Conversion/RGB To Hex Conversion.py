def calcular(rgb):
    if rgb > 255:
        rgb = 255
    elif rgb < 0:
        rgb = 0
    rgb = hex(rgb)[2:].upper()
    if len(rgb) < 2:
        rgb = "0" + rgb
    return rgb    

def rgb(r, g, b):
    return calcular(r) + calcular(g) + calcular(b)