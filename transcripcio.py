from re import sub

def trans_cod(cadena:str):
    '''
        Devuelve la secuencia de ARNm a partir de la
        cadena codificante de ADN
    '''
    return sub(r'T',r'U',cadena)

def trans_mol(cadena:str):
    '''
        Devuelve la secuencia de ARNm a paritr de la
        cadena molde de ADN
    '''
    for i in range(len(cadena)):
        if cadena[i] == 'A':
            cadena = cadena[:i] + 'U' + cadena[i+1:]
        elif cadena[i] == 'T':
            cadena = cadena[:i] + 'A' + cadena[i+1:]
        elif cadena[i] == 'C':
            cadena = cadena[:i] + 'G' + cadena[i+1:]
        elif cadena[i] == 'G':
            cadena = cadena[:i] + 'C' + cadena[i+1:]
    return cadena