listanombre=[]
listaApellido=[]
listaCargo=[]
def registrarTrabajador():
    nombre=input("Ingrese su nombre: ")
    listanombre.append(nombre)
    apellido=input("Ingrese su apellido: ")
    listaApellido.append(apellido)
    while True:
        cargo=input("Ingrese su cargo\n1.-CEO\n2.-Desarrollador\n3.-Analista de datos\n: ")
        if cargo==1:
            cargo="CEO"
            listaCargo.append(cargo)
            break
        elif cargo==2:
            cargo="Desarrollador"
            listaCargo.append(cargo)
            break
        elif cargo==3:
            cargo="Analista de datos"
            listaCargo.append(cargo)
            break
        else:
            print("Dato no valido")
mi_texto = "../texto.txt"
with open(mi_texto, 'a+') as f:
    for i in listanombre:
        f.write(i)
with open(mi_texto, 'a+') as f:
    for i in listaApellido:
        f.write(i)
with open(mi_texto, 'a+') as f:
    for i in listaCargo:
        f.write(i)
def listaTodosLosTrabajadores():
    
    def planillaSueldo():
        print("si")