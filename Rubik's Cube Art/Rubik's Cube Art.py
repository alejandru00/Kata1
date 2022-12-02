def cube(n):
    ladoarriba = '/\\' 
    completararriba = '_\\' 
    ladoabajo = '\\/'
    completarabajo = '_/' 
    
    espacioenblanco = ''
    for row in range(n):
        espacioenblanco += (n-row-1)*' ' + (row+1) * ladoarriba + n * completararriba + '\n'
    for row in reversed(range(n)):
        espacioenblanco += (n-row-1)*' ' + (row+1) * ladoabajo + n * completarabajo + '\n'
        
    return espacioenblanco[:-1]

print(cube(n))