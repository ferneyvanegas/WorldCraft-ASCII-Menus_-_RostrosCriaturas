'''
    Desarrollado por: Ferney Vanegas Hernández
    Misión TIC 2022
    Versión : 1.0.1
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
    while exit == False:
        print(
            '************************\n'
            'Elije tu destino (Ej: 1):\n'
            '************************\n'
            '1. Crear Rostro\n'
            '2. Listar Rostros\n'
            '3. Buscar Rostro\n'
            '4. Salir del Sistema\n'
            '************************'
        )
        opt = input('-> ')

        if opt.isdigit():
            if int(opt) == 1:
                c.create_face()
            if int(opt) == 2:
                s.list_faces()
            if int(opt) == 3:
                face_name = input('Ingresa el nombre del rostro que deseas abrir\n->')
                if not s.find_face(face_name):
                    print('Rostro no encontrado...\n')
            if int(opt) == 4:
                # La única opción que habilita la salida
                exit = True

main()
            