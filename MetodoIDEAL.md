# WorldCraft ASCII: Parte 4
> **Autor: Ferney Vanegas Hernández**

> **Misión TIC 2022**

> **Reto: 6**

## **Contexto**
El juego WorldCraft ASCII se hace cada vez más popular. Ahora que los niveles están poblados con criaturas y jugadores, se hace imprescindible darles un rostro a cada uno de ellos.

## PROBLEMA (I)
### **El problema**
No existe un rostro para ninguna de las criaturas del juego WorldCraft ASCII ni tampoco para los jugadores
### **Objetivos**
* Proporcionar opciones al usuario para:
    * Crear rostros
    * Guardar rostros
    * Listar rostros creados
    * Consultar rostros específicos
* Los rostros creados deben quedar guardados en la memoria secundaria del sistema (archivos en el DD)
### **Interesados**
* Los jugadores y aficionados del juego WorldCraft ASCII
### **Restricciones**
* Las características para la creación de los rostros deben estar en archivos .txt
* Las líneas en los archivos deben seguir el modelo siguiente:
    * Línea 1: Cabello
    * Línea 2: Ojos
    * Línea 3: Orejas y Nariz
    * Línea 4: Boca
    * Línea 5: Cuello
* Para crear un rostro, debe haberse escogido una opción para cada rasgo dado
* Para crear un rostro, debe haberse asignado un nombre al mismo, diferente de otro existente

## DEFINICIÓN (D)
### **Información Suministrada**
* Se debe ofrecer opciones para crear un rostro:
    * Selección de cabello
        * Ofrecer opciones de cabello
    * Selección de ojos
        * Ofrecer opciones de ojos
    * Selección de orejas y nariz
        * Ofrecer opciones de orejas y narices
    * Selección de boca
        * Ofrecer opciones de bocas
    * Selección de cuello
        * Ofrecer opciones de cuellos
* La construcción del rostro debe ir viéndose en tiempo real
* El rostro debe quedar guardado codificado en un archivo txt
* El archivo debe tener un nombre que el usuario le asigne
* El sistema debe mostrar un listado de los rostros guardados
* El sistema debe permitir buscar un rostro por su nombre
* La siguiente ﬁgura muestra el rostro y su respectiva codiﬁcación:
![ej](img/ej.jpg 'Ejemplo')
### **Información Requerida**
* Un patrón adecuado para guardar la codificación del rostro, que se ajuste a lo dado, y que permita ser decodificado con un algoritmo
* Manejo de archivos en el lenguage Python
* Manejo de listas, tuplas y matrices en Python
* Lectura de directorios con Python
### **Subproblemas**
* Ofrecer opciones para la creación de rostros (sobre rasgos)
* Permitir que los rostros creados sean almacenados
* Permitir que el usuario consulte los rostros almacenados
* Permitir que el usuario busque un rostro específico

## ESTRATEGIA (E)
### **Ejemplo**
El siguiente ejemplo muestra el proceso de opciones y selección de las mismas para lograr crear, guardar, listar y consultar un rostro de ejemplo.
![ej2](img/ej2.jpg 'Ejemplo 2')
### **Estrategia**
* Ofrecer menú general al usuario:
    * Crear
    * Listar
    * Consultar por nombre
* Definir repositorios para cada rasgo del rostro a ofrecer
* Definir repositorio para guardar los rostros creados por el usuario
* Uso de lista para escribir opciones e ir mostrando construcción del rostro
* Al listar, buscar en los repositorios los nombres de los archivos y mostrarlos
* Al listar, seleccionar rostro por número
* Al buscar, seleccionar rostro por nombre

## ALGORITMOS (A)

### **Algoritmo decode_line**
*Parámetros: line_code*
* Funcion line<-decode_line()
    * line=''
    * Para cada i<-1 hasta Llamar longitud(line_code) con Paso 1 Hacer:
        * Para cada j<-0 hasta line_code[i][0] con Paso 1 Hacer:
            * line+=codes[1]
        * FinPara
    * FinPara
    * Retornar line
* FinFuncion
***
### **Algoritmo get_feature**
*Parámetros: feature*
* Funcion decode_line, style  | False <- get_feature()
    * Dimensionar styles []
    * file = Llamar open('path/"feature".txt')
    * Para cada i<-0 hasta Llamar longitud_lineas(file) con Paso 1 Hacer:
        * styles[i] = file[i]
    * FinPara
    * Para cada i<-0 hasta Llamar longitud(styles) con Paso 1 Hacer:
        * Escribir i+1.- styles[i][0] decode_line(styles[i])
    * FinPara
    * Escribir Llamar longitud(styles) + 1 . 'Volver'
    * Leer selection
    * Para cada i<-0 hasta Llamar longitud(styles) con Paso 1 Hacer:
        * Si selection == i-1 Entonces
            * Retornar decode_line(styles[i]), styles[i]
        * FinSi
    * FinPara
    * Retornar False
* FinFuncion
***
### **Algoritmo face_complete**
*Parámetros: face_requeriments*
* Funcion status<- face_complete()
    * status = True
    * Si False in face_requeriments Entonces:
        * status = False
    * FinSi
    * Retornar status
* FinFuncion
***
### **Algoritmo create_face()**
*Parámetros: Ninguno*
* Funcion create_face()
    * finish = False
    * Dimensionar face_requeriments[5]
    * face_requeriments[False, False, False, False, False]
    * Mientras finish==False Haga:
        * Escriba 'Elije un rasgo:'
        * Escriba '1. Cabello'
        * Escriba '2. Ojos'
        * Escriba '3. Orejas y Nariz'
        * Escriba '4. Boca'
        * Escriba '5. Cuello'
        * Escriba '6. Volver'
        * Si Llamar face_complete(face_requeriments) == True
            * Escriba '7. Guardar rostro'
        * FinSi
        * Leer rasgo
        * Si rasgo == 1 Entonces
            * face_requeriments[0] = Llamar get_feature(hair)
        * FinSi
        * Si rasgo == 2 Entonces
            * face_requeriments[1] = Llamar get_feature(eyes)
        * FinSi
        * Si rasgo == 3 Entonces
            * face_requeriments[2] = Llamar get_feature(ears_nose)
        * FinSi
        * Si rasgo == 4 Entonces
            * face_requeriments[3] = Llamar get_feature(mouth)
        * FinSi
        * Si rasgo == 5 Entonces
            * face_requeriments[4] = Llamar get_feature(neck)
        * FinSi
        * Si rasgo == 6 Entonces
            * finish=True
        * FinSi
        * Si rasgo == 7 and face_complete(face_requeriments) == True Entonces
            * Llamar save_face(face_requeriments)
            * finish=True
        * FinSi
        * Llamar draw_face(face_requeriments)
    * FinMientras
* FinFuncion
***
### **Algoritmo save_face**
*Parámetros: face_requeriments*
* Funcion save_face()
    * Escribir: 'Ingresa el nombre del rostro'
    * Leer face_name
    * open('path/"face_name".txt')
    * Para i<-0 hasta 4 con Paso 1 Hacer:
        * Escribir face_requeriments[i][1]
    * FinPara
    * close('path/"face_name".txt')
* FinFuncion
***
### **Algoritmo open_face**
*Parámetros: face_name*
* Funcion open_face
    * f = open('path/"face_name".txt')
    * Para i<-0 hasta 4 con Paso 1 Hacer:
        * Escribir Llamar decode_line(f[i])
    * FinPara
* FinFuncion
***
### **Algoritmo draw_face**
*Parámetros: face_requeriments*
* Funcion draw_face()
    * Para i<-0 hasta 4 con Paso 1 Hacer:
        * Escribir face_requeriments[i][0]
    * FinPara
* FinFuncion
***
### **Algoritmo list_faces**
*Parámetros: Ninguno*
* Funcion
    * Dimensionar faces_list = Llamar listar_ficheros()
    * Para i<-0 hasta Llamar longitud(faces_list) con Paso 1 Hacer:
        * Escribir i+1 faces_lists[i]
    * FinPara
    * Escribir Escoge el número de rostro que deseas ver, ó cualquier otra tecla para regresar al inicio
    * Leer opt_face
    * Para cada i<-0 hasta Llamar longitud(faces_list) con Paso 1 Hacer:
        * Si opt == i+1 Entonces
            * Retornar open_face(faces_lists[i])
        * FinSi
    * FinPara
    * Retornar False
* FinFuncion
***
### **Algoritmo find_face**
*Parámetros: Ninguho*
* Funcion find_face()
    * Leer face_name
    * Llamar open_face(face_name)
* FinFuncion
***
### **Algoritmo main**
*Parámetros: Ninguno*
* Funcion main()
    * exit=False
    * Mientras exit==False Haga:
        * Escriba 'Elije tu destino:'
        * Escriba '1. Crear'
        * Escriba '2. Listar'
        * Escriba '3. Buscar'
        * Escriba '4. Salir'
        * Leer = 1
        * Si opcion == 1 Entonces
            * Llamar create_face()
        * FinSi
        * Si opcion == 2 Entonces
            * Llamar list_faces()
        * FinSi
        * Si opcion == 3 Entonces
            * Llamar find_face()
        * FinSi
        * Si opcion == 4 Entonces
            * exit=True
        * FinSi
    * FinMientras
* FinFuncion
