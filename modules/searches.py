import os
import modules.create as c

def list_faces():
    '''
    Parameters:
    ----------
    Return:
    ----------
    '''
    faces_list = os.listdir('faces')
    print('\033[93m||||||||||||||||||||||||')
    print('|* LISTADO DE ROSTROS *|')
    print('||||||||||||||||||||||||\033[92m')
    for index,face in enumerate(faces_list):
        print(f'{index + 1}. {face}')
    print('\033[93m||||||||||||||||||||||||\033[0m')


def find_face(face_name:str):
    '''
    Parameters:
    * face_name: str
        El nombre de un archivo|rostro 
    ----------
    Return:
    * :bool
        True si el archivo existe
        False si el archivo no existe
    -----
    '''
    faces_list = os.listdir('faces')
    for face in faces_list:
        if f'{face_name}.txt' == face:
            print(c.open_face(face_name))
            return True
    return False
