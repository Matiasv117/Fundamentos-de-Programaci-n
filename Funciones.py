listanombre=[]
listaApellido=[]
listaCargo=[]
cont=0
def registrarTrabajador():
    nombre=input("Ingrese su nombre: ")
    listanombre.append(nombre)
    apellido=input("Ingrese su apellido: ")
    listaApellido.append(apellido)
    cont=1+cont
    while True:
        try:
            cargo=int(input("Ingrese su cargo\n1.-CEO\n2.-Desarrollador\n3.-Analista de datos\n: "))
        except:
            print("Opción invalida")
        else:
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
    archivo=open('Fundamentos-de-Programacion/texto.txt', 'a')
    archivo.write(f"{nombre},{apellido},{cargo}\n")
def listaTodosLosTrabajadores():
    for i in range(cont):
        print(f"{listanombre},{listaApellido},{listaCargo}\n")
def planillaSueldo():
        print("si")