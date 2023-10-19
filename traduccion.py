from re import findall

def conv_cod(codon:str):
    '''
        Convierte un codon dado a su
        aminoacido correspondiente
    '''
    tab_cod = {'UUU':'Phe','UUC':'Phe','UUA':'Leu', 'UUG':'Leu',
                'CUU':'Leu','CUC':'Leu','CUA':'Leu','CUG':'Leu',
                'AUU':'Iso','AUC':'Iso','AUA':'Iso','AUG':'Met',
                'GUU':'Val','GUC':'Val','GUA':'Val','GUG':'Val',
                'UCU':'Ser','UCC':'Ser','UCA':'Ser','UCG':'Ser',
                'CCU':'Pro','CCC':'Pro','CCA':'Pro','CCG':'Pro',
                'ACU':'Thr','ACC':'Thr','ACA':'Thr','ACG':'Thr',
                'GCU':'Ala','GCC':'Ala','GCA':'Ala','GCG':'Ala',
                'UAU':'Tyr','UAC':'Tyr','UAA':'STOP','UAG':'STOP',
                'CAU':'His','CAC':'His','CAA':'Gln','CAG':'Gln',
                'AAU':'Asn','AAC':'Asn','AAA':'Lys','AAG':'Lys',
                'GAU':'Asp','GAC':'Asp','GAA':'Glu','GAG':'Glu',
                'UGU':'Cys','UGC':'Cys','UGA':'STOP','UGG':'Try',
                'CGU':'Arg','CGC':'Arg','CGA':'Arg','CGG':'Arg',
                'AGU':'Ser','AGC':'Ser','AGA':'Arg','AGG':'Arg',
                'GGU':'Gly','GGC':'Gly','GGA':'Gly','GGG':'Gly'}
    return tab_cod[codon]
                

def trad(cadena:str):
    '''
        Devuelve la secuencia de aminoacidos
        a partir de la cadena de ARNm
    '''
    codones = findall(r'(\w{3})',cadena)
    amn = []
    for codon in codones:
        if conv_cod(codon) == 'STOP':
            break
        else:
            amn.append(conv_cod(codon))
    return '-'.join(amn)