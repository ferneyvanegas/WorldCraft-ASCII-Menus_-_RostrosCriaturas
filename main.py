import modules.create as c
import modules.searches as s

def main():
    '''
    Parameters:
    -----------
    Return:
    -----------
    '''
    exit = False
    while exit == False:
        print(
            'Elije tu destino:\n'
            '1. Crear\n'
            '2. Listar\n'
            '3. Buscar\n'
            '4. Salir\n'
        )
        opt = input('-> ')

        if opt.isdigit():
            if int(opt) == 1:
                c.create_face()
            if int(opt) == 2:
                print('Opción 2')
            if int(opt) == 3:
                print('Opción 3')
            if int(opt) == 4:
                exit = True

main()
            