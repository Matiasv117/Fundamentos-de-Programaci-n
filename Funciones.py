sueldoAFP=0
sueldoSALUD=0
listanombre=[]
listaApellido=[]
listaCargo=[]
listaSueldo= []
sueldobruto=[]
Desc_AFP=0.012
Desc_SALUD=0.007
def registrarTrabajador():
    nombre=input("Ingrese su nombre: ")
    listanombre.append(nombre)
    apellido=input("Ingrese su apellido: ")
    listaApellido.append(apellido)
    while True:
        try:
            cargo=int(input("Ingrese su cargo\n1.-CEO\n2.-Desarrollador\n3.-Analista de datos\n: "))
        except:
            print("Opción invalida")
        else:
            if cargo==1:
                cargo="CEO"
                sueldobruto=10000000
                listaSueldo.append(sueldobruto)
                listaCargo.append(cargo)
                break
            elif cargo==2:
                cargo="Desarrollador"
                sueldobruto=800000
                listaSueldo.append(sueldobruto)
                listaCargo.append(cargo)
                break
            elif cargo==3:
                cargo="Analista de datos"
                sueldobruto=750000
                listaSueldo.append(sueldobruto)
                listaCargo.append(cargo)
                break
            else:
                print("Dato no valido")
    archivo=open('Fundamentos-de-Programacion/texto.txt', 'a')
    archivo.write(f"{nombre},{apellido},{cargo},{sueldobruto}\n")
def listaTodosLosTrabajadores():
    for j in range(len(listanombre)):
        print(f"{listanombre},{listaApellido},{listaCargo},{listaSueldo}\n")
        print("-",end=" ")
def planillaSueldo():
    for i in range(len(listaSueldo)):
        sueldoAFP.append(listaSueldo[i] * Desc_AFP)
        sueldoSALUD.append(listaSueldo[i] * Desc_SALUD)
    print(sueldoAFP)
    print(sueldoSALUD)





