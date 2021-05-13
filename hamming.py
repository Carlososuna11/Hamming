""" 
    Codigo de Hamming para dummies
"""
from tabulate import tabulate

def Hamming_palabra_transmitir(codigo):
    """ 
    Codificar Mensaje
    """
    TIPO_BIT= ['M8','M7','M6','M5','M4','M3','M2','M1']
    TIPO_BIT_EXTENSO = ['M8','M7','M6','M5','C8','M4','M3','M2','C4','M1','C2','C1']
    TIPO_BIT_OUTPUT = ['TIPO DE BIT'] + TIPO_BIT_EXTENSO
    posicion = []
    dato = []
    cs = dict()
    for index,value in enumerate(codigo):
        cs[TIPO_BIT[index]] = int(value)
    cs['C1'] = cs['M1'] ^ cs['M2'] ^ cs['M4'] ^ cs['M5'] ^ cs['M7']
    cs['C2'] = cs['M1'] ^ cs['M3'] ^ cs['M4'] ^ cs['M6'] ^ cs['M7']
    cs['C4'] = cs['M2'] ^ cs['M3'] ^ cs['M4'] ^ cs['M8']
    cs['C8'] = cs['M5'] ^ cs['M6'] ^ cs['M7'] ^ cs['M8']
    for index,value in enumerate(TIPO_BIT_EXTENSO):
        dato.append(cs[value])
        posicion.append(index+1)
    posicion.sort(reverse=True)
    posicion = ['POSICION'] + posicion
    dato = ['DATO'] + dato
    print(tabulate([TIPO_BIT_OUTPUT,dato,posicion],tablefmt="fancy_grid"))
    
    
    # cs['M4'] = 1 
    # er = dict()
    # er['E1'] = cs['M1'] ^ cs['M2'] ^ cs['M4'] ^ cs['M5'] ^ cs['M7'] ^ cs['C1']
    # er['E2'] = cs['M1'] ^ cs['M3'] ^ cs['M4'] ^ cs['M6'] ^ cs['M7'] ^ cs['C2']
    # er['E4'] = cs['M2'] ^ cs['M3'] ^ cs['M4'] ^ cs['M8'] ^ cs['C4']
    # er['E8'] = cs['M5'] ^ cs['M6'] ^ cs['M7'] ^ cs['M8'] ^ cs['C8']

    # error = int(f"0b{er['E8']}{er['E4']}{er['E2']}{er['E1']}",2)
    # print(er)
    # print(error)

def Hamming_error(codigo):
    """
    DECODIFICAR MENSAJE
    """
    TIPO_BIT_EXTENSO = ['M8','M7','M6','M5','C8','M4','M3','M2','C4','M1','C2','C1']
    TIPO_BIT_OUTPUT = ['TIPO DE BIT'] + TIPO_BIT_EXTENSO
    cs = dict()
    for index,value in enumerate(codigo):
        cs[TIPO_BIT_EXTENSO[index]] = int(value)
    er = dict()
    er['E1'] = cs['M1'] ^ cs['M2'] ^ cs['M4'] ^ cs['M5'] ^ cs['M7'] ^ cs['C1']
    er['E2'] = cs['M1'] ^ cs['M3'] ^ cs['M4'] ^ cs['M6'] ^ cs['M7'] ^ cs['C2']
    er['E4'] = cs['M2'] ^ cs['M3'] ^ cs['M4'] ^ cs['M8'] ^ cs['C4']
    er['E8'] = cs['M5'] ^ cs['M6'] ^ cs['M7'] ^ cs['M8'] ^ cs['C8']
    error = int(f"0b{er['E8']}{er['E4']}{er['E2']}{er['E1']}",2)
    if error-1 != -1:
        
        posicion = []
        anterior = []
        dato = []
        for index,value in enumerate(TIPO_BIT_EXTENSO):
            anterior.append(cs[value])
            posicion.append(index+1)
        anterior = ['MENSAJE RECIBIDO CON ERROR'] + anterior
        pos_error = TIPO_BIT_EXTENSO[-error]
        cs[pos_error] = (lambda x: 1 if x==0 else 0)(cs[pos_error])
        
        for index,value in enumerate(TIPO_BIT_EXTENSO):
            dato.append(cs[value])
        posicion.sort(reverse=True)
        posicion = ['POSICION'] + posicion
        dato = ['MENSAJE ARREGLADO'] + dato

        print('Upss! Parece que hay un error ')
        print(f'Ubicacion del Error: posicion {error}')
        print(tabulate([TIPO_BIT_OUTPUT,anterior,dato,posicion],tablefmt="fancy_grid"))
    else:
        print('No hay Error! crack')


if __name__ == '__main__':
    codigo  = '001011101000'
    Hamming_error(codigo)
    # Hamming_palabra_transmitir(codigo)