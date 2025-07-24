global nombre, numero
nombre=[]
numero=[]
def menu():
    while True:
        try:
            print("-"*50)
            print("\t\t\t\tAGENDA DE CONTACTOS")
            print("1. Agregar contactos")
            print("2. Ver contactos")
            print("3. Buscar contactos")
            print("4. Eliminar contactos")
            print("5. salir")
            op=int(input("ingrese una opcion deseada: "))
            if op>5 or op<1:
                print("\t\t\t\terror, vuelva a ingresar")
            else:
                break
        except ValueError:
                print("\t\t\t\terror, vuelva a ingresar")

    match op:
        case 1:
            print("-"*50)
            agregar()
        case 2:
            print("-"*50)
            ver()
        case 3:
            print("-"*50)
            buscar()
        case 4:
            print("-"*50)
            eliminar()
        case 5:
            print("\n\t\t\tHASTA PRONTO")

def agregar():
    while True:
        while True:
            try:
                contc=input("ingrese el nombre: ")
                contcmayusc=contc.upper()
                nombre.append(contcmayusc)
                break
            except ValueError:
                print("\t\t\t\terror, vuelva a ingresar")
        while True:
            try:
                num=input("ingrese el numero de telefono: ")
                if not num.isdigit() or len(num) != 9:
                    print("ERROR, solo se aceptan 9 digitos")
                else:
                    numero.append(num)
                    break
            except ValueError:
                print("\t\t\t\terror, vuelva a ingresar")
        while True:
            otravez=input("desear agregar otro contacto mas?:")
            otravezmayusc=otravez.upper()
            if otravezmayusc!="SI" and otravezmayusc!="NO":
                print("error, vuelve a ingresar")
            else:
                break
        if otravezmayusc=="SI":
            continue
        if otravezmayusc=="NO":
            menu()
            break
            

def ver():
    global numero, nombre
    if not nombre and not numero:
        print("\t\t\t NO HAY CONTACTOS REGISTRADOS")
        menu()
    print("\t\t\t REGISTRO DE CONTACTOS AGREGADOS")
    for n,p in zip(nombre, numero):
        print(f"{n} : {p}")
    menu()

def buscar():
    global nombre,numero
    if not nombre and not numero:
        print("\t\t\t NO HAY CONTACTOS REGISTRADOS")
        menu()
    while True:
        try:
            busc=input("seleccione el nombre o numero de la persona: ")
            buscmayusc=busc.upper()
            if buscmayusc in nombre:
                indice=nombre.index(buscmayusc)
                numbuscado=numero[indice]
                print(f"{buscmayusc} : {numbuscado}")
                break
            else:
                print("\t\t\terror, nombre no encontrado")
            
        except ValueError:
            print("\t\t\t\terror, vuelva a ingresar")
    menu()

def eliminar():
    if not nombre and not numero:
        print("\t\t\t NO HAY CONTACTOS REGISTRADOS")
        menu()
    print("\t\t\t REGISTRO DE CONTACTOS AGREGADOS")
    contador=0
    for n,p in zip(nombre, numero):
        print(f"{contador}. {n} : {p}")
        contador=contador+1
    while True:
        try:
            elim=int(input(f"ingrese el contacto a eliminar(del 0 al {contador-1}): "))
            nombre.pop(elim)
            numero.pop(elim)
            print(f"El contacto ha sido elliminado con exito")
            break

        except ValueError:
            print("\t\t\t\terror, vuelva a ingresar")
    menu()
def ejecutar():
    menu()
ejecutar()  