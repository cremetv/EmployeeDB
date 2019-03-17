import math

print("Base Informativa de Obreros:")
print("...")

employeeList = {"001": ("Hester", 12), "002": ("Gavin", 34), "003": ("Kelsey", 9)
                }

spacer = str("\n\n\n\n\n")

while True:
    print("Opciones:")
    print("1 -  Mira Todos los Obreros\n2 - Cambiar Dato de Obreros\n3 - Agregar Obreros Nuevos\n4 - Buscar por Informacion\n5 - Salir")
    print("...")
    menu = int(input("Escribir: "))

    if menu == 5:
        break
    
    elif menu == 1:
        print("\n")
        print("Numero de ID: Nombre de Obrero")

        for key, value in employeeList.items():
            print("{}: {}".format(key, employeeList[key][0]))
            print("    Horas Trabajadas: ", employeeList[key][1])
        
        print("...")
        any_key = input("Escribe alguna boton a continuar.\n")
        print(spacer)

    elif menu == 2:
        print("\n")
        print("Cambiar Dato:")
        modID = str(input("Escribir ID: "))
        print("Ok, el nombre de este obrero es: {}".format(employeeList[modID][0]))
        newName = str(input("Escribir un nombre nuevo: "))
        newHW = int(input("¿Cuantas horas estuvo este obrero trabajo?: "))
        employeeList[modID] = (newName, newHW)
        print("\n")
        print("El Dato del Obrero ID#{} esta Cambiada:".format(modID))
        print("Nombre: {}".format(newName))
        print("Horas Trabajadas: {}".format(newHW))
        print("...")
        any_key = input("Escribe alguna boton a continuar.\n")
        print(spacer)

    elif menu == 3:
        print("\n")
        print("Construir Dato de un Obrero Nuevo:")
        name = str(input("Escribir el Nombre de Obrero: "))
        hw = int(input("Horas Trabajadas: "))
        idNum = str(input("Numero de ID: "))
        employeeList[idNum] = (name, hw)
        print("\n")
        print("Un Dato de un Obrero Nuevo esta Construida:")
        print("{}: {} - {} Horas Trabajadas".format(idNum, name, hw))
        print("...")
        any_key = input("Escribe alguna boton a continuar.\n")
        print(spacer)

    elif menu == 4:
        print("\n")
        print("Buscar el Base Informativa por:")
        print("1 - Nombre del Obrero\n2 - Numero de ID del Obrero")
        searchMenu = int(input("Escribir: "))

        if searchMenu == 1:
            print("Este habilidad no esta hay todavia.")
            print("\n")
        elif searchMenu == 2:
            print("Este habilidad no esta hay todavia.")
            print("\n")
        else:
            print("La programa no se que tu escribiste. Proba un otra vez.")
            print("\n")

    else:
        print("La programa no se que tu escribiste. Proba un otra vez.")
        print("\n")
        
        
        
        
    
