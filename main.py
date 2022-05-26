'''
    Desarrollado por: Ferney Vanegas Hernández
    Misión TIC 2022
    Versión : 1.0.2
    Título: Reto 6
'''
import modules.create as c
import modules.searches as s

def main():
    '''
    Parameters:
    -----------
    Return:
    -----------
    '''
    exit = False # Flag

    # Colores
    '''
        OK = '\033[92m' #GREEN
        WARNING = '\033[93m' #YELLOW
        FAIL = '\033[91m' #RED
        RESET = '\033[0m' #RESET COLOR
        Fuente: https://www.delftstack.com/es/howto/python/python-print-colored-text/
    '''
    
    while exit == False:
        print(
            '\033[93m************************\n'
            'Elije tu destino (Ej: 1):\n'
            '************************\n'
            '\033[92m1. Crear Rostro\n'
            '2. Listar Rostros\n'
            '3. Buscar Rostro\n'
            '\033[91m4. Salir del Sistema\n'
            '\033[93m************************'
        )
        opt = input('-> \033[0m')

        if opt.isdigit():
            if int(opt) == 1:
                c.create_face()
            if int(opt) == 2:
                s.list_faces()
            if int(opt) == 3:
                face_name = input('Ingresa el nombre del rostro que deseas abrir\n-> ')
                if not s.find_face(face_name):
                    print('\033[91mRostro no encontrado...\033[0m\n')
            if int(opt) == 4:
                # La única opción que habilita la salida
                exit = True

main()
            