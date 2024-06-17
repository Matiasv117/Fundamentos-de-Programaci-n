
#Crear archivo, w es permiso de escritura
#Las comillas al inciio y 3 al final del texto representa un texto
#Con saltos de linea
datos = """Este es un archivo de texto simple que no tiene
ningún formato en particular, lo podemos utilizar
para guadar todo tipo de texto"""

#Se crea el contexto para abrir un archivo nuevo
lista=[]
with open('archivo_nuevo.txt','w',) as luisemilio:
    luisemilio.write(datos)


#opcion 2
#usando el conteto with el archivo se cierra automaticamente
with open('clase16/archivo.txt','r',encoding='utf-8') as archivo:
    contenido = archivo.read()
print(contenido)
