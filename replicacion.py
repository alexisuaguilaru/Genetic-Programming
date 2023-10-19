def repli(cadena:str):
    '''
        Devuelve la cadena hija a partir de una
        cadena molde de ADN
    '''
    for i in range(len(cadena)):
        if cadena[i] == 'A':
            cadena = cadena[:i] + 'T' + cadena[i+1:]
        elif cadena[i] == 'T':
            cadena = cadena[:i] + 'A' + cadena[i+1:]
        elif cadena[i] == 'C':
            cadena = cadena[:i] + 'G' + cadena[i+1:]
        elif cadena[i] == 'G':
            cadena = cadena[:i] + 'C' + cadena[i+1:]
    return cadena