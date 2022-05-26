import modules.features as f

def create_face():
    '''
    Parameters:
    ----------
    ----------
    Return:
    ----------
    '''
    finish = False
    face_requeriments = [False, False, False, False, False]
    while finish == False:
        print(
            '\033[93m************************\n'
            'Elige un rasgo (Ej: 1):\n'
            '************************\n'
            '\033[0m1. Cabello\n'
            '2. Ojos\n'
            '3. Orejas y Nariz\n'
            '4. Boca\n'
            '5. Cuello\n'
            '\033[91m6. Volver'
        )
        # Esta opción solo está disponible si se han llenado todos los rasgos necesarios para crear el rostro
        if face_complete(face_requeriments) == True:
            print('\033[92m7. Guardar rostro')
        print('\033[93m************************')
        
        feature = input('-> \033[0m')

        if feature.isdigit():
            if int(feature) == 1:
                face_requeriments[0] = f.get_feature('hair')
            if int(feature) == 2:
                face_requeriments[1] = f.get_feature('eyes')
            if int(feature) == 3:
                face_requeriments[2] = f.get_feature('ears_nose')
            if int(feature) == 4:
                face_requeriments[3] = f.get_feature('mouth')
            if int(feature) == 5:
                face_requeriments[4] = f.get_feature('neck')
            if int(feature) == 6:
                finish = True
            if int(feature) == 7 and face_complete(face_requeriments) == True:
                save_face(face_requeriments)
                finish = True
            draw_face(face_requeriments)


def face_complete(face_requeriments:list):
    '''
    Parameters:
    ----------
    * face_requeriments: list
        Lista con una longitud de 5 puestos
    ----------
    Return:
    ----------
    * : bool
        True: Si no se encontró ningún False almacenado en face_requeriments
        
        False: Si se encontró ningún False almacenado en face_requeriments
    '''
    status = True
    if False in face_requeriments:
        status = False
    return status

def draw_face(face_requeriments):
    '''
    Parameters:
    ----------
    * face_requeriments: list
        Lista con una longitud de 5 puestos
        Cada puesto tiene una lista de 2 puestos
            Puesto 1: Contiene un string con un rasgo decodificado
            Puesto 2: Contine una lista con los códigos para crear un rasgo
    ----------
    Return:
    ----------
    ''' 
    print('\033[93m------------')
    print('|||ROSTRO|||')
    print('------------\033[92m')
    for line in face_requeriments:
        if line == False:
            print('\n')
        else:
            print(line[0])
    print('\033[93m------------\033[0m')

def save_face(face_requeriments):
    '''
    Parameters:
    ----------
    * face_requeriments: list
        Lista con una longitud de 5 puestos
        Cada puesto tiene una lista de 2 puestos
            Puesto 1: Contiene un string con un rasgo decodificado
            Puesto 2: Contine una lista con los códigos para crear un rasgo
    ----------
    Return:
    ----------
    ''' 
    face_name = input('Ingresa el nombre del rostro:\n->')
    file = open(f'faces/{face_name}.txt','w')
    for line in face_requeriments:
        # Creación y 'purificación' de las líneas
        # =============================================
        l = ''
        for index, i in enumerate(line[1]):
            # El primer elemento es el nombre del rasgo. No se necesita registrar
            # Sin embargo, se envía una coma, pues la función decode_line que sirve
            # Para leer decodificar líneas, está esperando una posición cero
            if index == 0:
                l+=f','
            else:
                l+=f'{i},'
        l = l[:-1] # Se elimina la última coma (,)
        # =============================================
        file.write(f'{l}\n')
    file.close()

def open_face(face_name:str):
    '''
    Parameters:
    ----------
    * face_name: str
        Nombre del archivo para abrir
    ----------
    Return:
    ----------
    '''
    file = open(f'faces/{face_name}.txt')
    print('\033[93m------------')
    # Poner el nombre en mayúsculas
    print(f'|||{face_name.upper()}|||')
    print('------------\033[92m')
    for line in file:
        # La función decode_line requiere un listado con los códigos
        print(f.decode_line(line.split(',')))
    print('\033[93m------------\033[0m')
    

