global nombre, numero
nombre=[]
numero=[]
def menu():
    
    while True:
        try: 
            print("\t\t\tMENU PRINCIPAL")
            print("1. agregar contactos")
            print("2. ver contactos")
            print("3. eliminar contactos")
            print("4. buscar contactos")
            print("5. salir")
            op=int(input("ingrese una opcion: "))
            if op<1 or op>5:
                print("error, numero fuera de rango")
            else:
                break
        except ValueError:
            print("error, no se aceptan otros digitos ")
    
    match op:
        case 1:
            agregar()
        case 2:
            ver()
        case 3:
            eliminar()
        case 4:
            buscar()
        case 5:
            print("gracias,  vuelva pronto")

        
def agregar():
    
    while True:
        while True:
            try:
                nombre=input("ingrese el nombre:")
                nombreMayusc=nombre.upper()
                nombre.append(nombreMayusc)
                break
            except ValueError:
                print("error, no se acpetan otros digitos")
        while True:
            try: 
                num=int(input("ingrese el numero: "))
                if not num.isdigit or len(num)!=9:
                    print("ingrese de nuevo")
                else:
                    numero.append(num)
                    break
            except ValueError:
                print("error, no se admiten otros digitos")
        while True:
            cont=input("desea seguir agregando?: ")
            contMa=cont.upper()
            if contMa!="SI" and contMa!="NO":
                print("escriba si o no")
            else:
                break
        if contMa=="SI":
            continue
        if contMa=="NO":
            menu()
            break

def ver():
    global numero, nombre
    if not numero or not nombre:
        print("error, CONTACTOS VACIOS")
        menu()
    print("\t\tCONTACTOS REGISTRADOS")
    contador=0
    for n,p in zip(nombre,numero):
        print(f"{contador}. {n}->{p}")
        contador=contador+1
    
    menu()



def eliminar():
    global nombre, numero
    if not numero or not nombre:
        print("error, CONTACTOS VACIOS")
        menu()
    print("\t\tCONTACTOS REGISTRADOS")
    contador=0
    for n,p in zip(nombre,numero):
        print(f"{contador}. {n}->{p}")
        contador=contador+1
    
    while True:
        try:
            o=int(input(f"ingrese una opcion del (0 al {contador-1}): "))
            if o>contador-1 or o<0:
                print("numero fuera de rango")
            else:
                nombre.pop(o)
                numero.pop(o)
                print("\t\tCONTACO ELIMINADO CON EXITO")
                break
        except ValueError:
            print("digitos erroneos ingresados")
    menu()

def buscar():
    global nombre, numero
    if not numero or not nombre:
        print("error, CONTACTOS VACIOS")
        menu()
    
    while True:
        try:
            busc=input("ingrese el nombre a buscar: ")
            buscMayu=busc.upper()
            if buscMayu in nombre:
                print("\t\tCONTACTO ENCONTRADO")
                indice=nombre.index(buscMayu)
                numbusc=numero[indice]
                print(f"{buscMayu}->{numbusc}")
                break
            else:
                print("contacto no encontrado")
        except ValueError:
            print("error, digitos erroneos ingresados")
    menu()

menu()
