import base64
import hashlib
import os
def pedirNumeroEntero():
    correcto = False
    num = 0
    print('Formatos disponibles a eleccion (Numeros,MD5,SHA1,BASE64)')
    print('Extensiones Integradas (txt,pdf,docx y xlxs)')
    while (not correcto):
        try:
            num = int(input("Introduce una opcion para descargar un archivo: "))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')
    return num
salir = False
opcion = 0
numeros = []
ruta="D:/nicol/Documents/"
messaje='Archivo descargado con exito en la siguiente ruta '+ruta
while not salir:
    print("1. Imprimir MD5")
    print("2. Imprimir SHA1")
    print("3. Imprimir BASE64")
    print("4. Imprimir Solo numeros")
    print("5. Imprimir TODOS")
    print("6. Salir")
    opcion = pedirNumeroEntero()
    if opcion == 1:
        file = open(ruta+"md5Diccionario.txt", "w")
        for x in range(0, 10001):
            parseo = str(x)
            file.write(hashlib.md5((parseo).encode('utf-8')).hexdigest()+'.txt'+os.linesep)
            file.write(hashlib.md5((parseo).encode('utf-8')).hexdigest()+'.pdf'+os.linesep)
            file.write(hashlib.md5((parseo).encode('utf-8')).hexdigest()+'.docx'+os.linesep)
            file.write(hashlib.md5((parseo).encode('utf-8')).hexdigest()+'.xlxs'+os.linesep)
        file.close()
        print(messaje)
    elif opcion == 2:
        file = open(ruta+"sha1Diccionario.txt", "w")
        for x in range(0, 10001):
            parseo = str(x)
            file.write(hashlib.sha1((parseo).encode('utf-8')).hexdigest()+'.txt'+os.linesep)
            file.write(hashlib.sha1((parseo).encode('utf-8')).hexdigest()+'.pdf'+os.linesep)
            file.write(hashlib.sha1((parseo).encode('utf-8')).hexdigest()+'.docx'+os.linesep)
            file.write(hashlib.sha1((parseo).encode('utf-8')).hexdigest()+'.xlxs'+os.linesep)
        file.close()
        print(messaje)
    elif opcion == 3:
        file = open(ruta+"base64Diccionario.txt", "w")
        for x in range(0, 10001):
            parseo = str(x)
            encodedBytes = base64.b64encode(parseo.encode("utf-8"))
            file.write(str(encodedBytes, "utf-8")+'.txt'+os.linesep)
            file.write(str(encodedBytes, "utf-8")+'.pdf'+os.linesep)
            file.write(str(encodedBytes, "utf-8")+'.docx'+os.linesep)
            file.write(str(encodedBytes, "utf-8")+'.xlxs'+os.linesep)
        file.close()
        print(messaje)
    elif opcion==4:
        file = open(ruta+"numerosDiccionario.txt", "w")
        for x in range(0, 10001):
            parseo = str(x)
            file.write(parseo+'.txt'+os.linesep)
            file.write(parseo+'.pdf'+os.linesep)
            file.write(parseo+'.docx'+os.linesep)
            file.write(parseo+'.xlxs'+os.linesep)
        file.close()
        print(messaje)
    elif opcion == 6:
        salir = True
    else:
        print("Introduce un numero entre 1 y 5")
print("Fin")