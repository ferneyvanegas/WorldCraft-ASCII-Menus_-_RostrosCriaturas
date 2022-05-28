import os

def get_feature(feature:str):
    '''
    Parameters:
    ----------
    * features: str
        El nombre del rasgo que desea obtener
    ----------
    Return:
    ----------
    * :tuple
        Tupla con la siguiente información
        1)_ :str
            Una cadena de texto con el rasgo decodificado
        2) style: list
            Lista con los códigos para crear un rasgo
    * False: bool
        El usuario no escogió ninguna opción 
    ----------
    '''
    styles = []
    # Los rasgos están almacenados en archivos de texto con el mismo nombre
    file = open(f'repos/{feature}.txt')
    for line in file:
         # Quito los saltos de línea y divido en lista
        styles.append(line.rstrip('\n').split(',')) 
    # Mostrar opciones a usuario
    for index, style in enumerate(styles):
        print(f'{index + 1}. \033[93m{style[0]} \t: \033[92m{decode_line(style)}\033[0m')
    print(f'{len(styles) + 1}. \033[91mVolver|Borrar\n')
    print('\033[93mEscoge una opción (Ej:1):')
    selection = input('-> \033[0m')
    if selection.isdigit():
        for index, style in enumerate(styles):  
            if index == int(selection) - 1:
                return  decode_line(style), style
    return False

def decode_line(line_code:list):
    '''
    Parameters:
    ----------
    * line_code: list
        Lista con los códigos para crear un rasgo
    ----------
    Return:
    ----------
    * line: str
        Una cadena de texto con el rasgo decodificado
    '''
    line = ''
    for i in range(1, len(line_code)):
        for j in range(int(line_code[i][0])):
            line+=line_code[i][1]
    return line

def set_creature_name():
    '''
    Parameters:
    ----------
    Return:
    ----------
    * face_name: str
        Cadena de texto con un nombre válido
    '''
    correct_name=False # Flag
    while correct_name == False:
        exist = False
        face_name = input(
        '\033[93mIngresa el nombre del rostro:\n'
        '(Al menos 1 caracter)\n ->\033[0m'
        )
        # El nombre no pueden ser solo espacios y además debe tener al menos 1 caracter
        if len(face_name.strip()) > 0:
            faces_list = os.listdir('faces')
            for face in faces_list:
                if f'{face_name}.txt' == face:
                    exist = True
            if not exist:
                return face_name
            else:
                print('\033[91mError: Ya existe un rostro con este nombre. Prueba otro por favor\033[0m')
        else:
            print('\033[91mError: El nombre no pueden ser solo espacios y además debe tener al menos 1 caracter\033[0m')
