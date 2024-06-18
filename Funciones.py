sueldoAFP=0
sueldoSALUD=0
listanombre=[]
listaApellido=[]
listaCargo=[]
listaSueldo= []
listaSueldoLiquido=[]
Desc_AFP=0.88
Desc_SALUD=0.003
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
            print(f"{listanombre}\n{listaApellido}\n{listaCargo}\n{listaSueldo}\n")
def planillaSueldo():
        cargo=int(input("Ingrese su cargo\n1.-CEO\n2.-Desarrollador\n3.-Analista de datos\n: "))
        if cargo==1:
            sueldobruto=10000000
            sueldoliquido=sueldobruto*Desc_AFP
            resultado=sueldoliquido*Desc_SALUD
            listaSueldoLiquido.append(resultado) 
            for j in range(len(listanombre)):
                print(f"{listanombre}\n{listaApellido}\n{listaCargo}\n{listaSueldoLiquido}\n")
  
        elif cargo==2: 
            sueldobruto=800000
            sueldoliquido=sueldobruto*Desc_AFP
            resultado=sueldoliquido*Desc_SALUD
            listaSueldoLiquido.append(resultado)
            for j in range(len(listanombre)):
                print(f"{listanombre}\n{listaApellido}\n{listaCargo}\n{listaSueldoLiquido}\n")

        elif cargo==3:
            sueldobruto=750000
            sueldoliquido=sueldobruto*Desc_AFP
            resultado=sueldoliquido*Desc_SALUD
            listaSueldoLiquido.append(resultado)
            for j in range(len(listanombre)):
                print(f"{listanombre}\n{listaApellido}\n{listaCargo}\n{listaSueldoLiquido}\n")
        else:
            print("Dato no valido")




