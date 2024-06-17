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
def listaTodosLosTrabajadores():
    
def planillaSueldo():
