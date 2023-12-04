print("Bienvenidos a la biblioteca del Sena \n")
nombre = input("Cual es su nombre Nombre \n")
print(nombre, "aqui puedes consultar Los Siguientes Libros:\n")
print("1-Libros de Novelas\n""2-Libros de Misterio\n""3-Libros de policíaca\n""4-Libros de Ingles\n""5-Libros de Fisica\n")
num = int(input("seleccione su opcion\n"))
if num == 1:
    print("la opcion que seleccionaste fue Novelas\n")
    print("Tenemos disponibles los siguientes libros de Novelas\n")
    print("-------------------------------------------------------\n|  ID  |          Nombre          |      Autor        |\n------------------------------------------------------\n|  01  |Don Quijote de la mancha  |Migel de Cervantes |\n|  02  |La carretera              |Cormac McCarthy    |\n|  03  |Criadas & Señoras         |Kathryn Stockett   |\n|  04  |Crematorio                |Rafael Chirbes     |\n|  05  |Un árbol crece en Brooklyn|Betty Smith        |\n|  06  |Los hermanos Karamázov    |Fiodor Dostoievski |\n------------------------------------------------------\n")
while True:
    num1 = int(input("¿Cuál es el informacion del libro que deseas elegir? (Ingresa 0 para salir):\n"))

    if num1 == 0:
        print("Saliendo del programa...")
        break
    elif num1 == 1:
        print("-------------------------------------------------------\n|  ID  |          Nombre          |      Autor        |\n------------------------------------------------------\n|  01  |Don Quijote de la Mancha  |Miguel de Cervantes |\n------------------------------------------------------\n")
    elif num1 == 2:
        print("-------------------------------------------------------\n|  ID  |          Nombre          |      Autor        |\n------------------------------------------------------\n|  02  |La carretera              |Cormac McCarthy    |\n------------------------------------------------------\n")
    elif num1 == 3:
        print("-------------------------------------------------------\n|  ID  |          Nombre          |      Autor        |\n------------------------------------------------------\n|  03  |Criadas & Señoras         |Kathryn Stockett   |\n------------------------------------------------------\n")
    elif num1 == 4:
        print("-------------------------------------------------------\n|  ID  |          Nombre          |      Autor        |\n------------------------------------------------------\n|  04  |Crematorio                |Rafael Chirbes     |\n------------------------------------------------------\n")
    elif num1 == 5:
        print("-------------------------------------------------------\n|  ID  |          Nombre          |      Autor        |\n------------------------------------------------------\n|  05  |Un árbol crece en Brooklyn|Betty Smith        |\n------------------------------------------------------\n")
    elif num1 == 6:
        print("-------------------------------------------------------\n|  ID  |          Nombre          |      Autor        |\n------------------------------------------------------\n|  06  |Los hermanos Karamázov    |Fiodor Dostoievski |\n------------------------------------------------------\n")
    else:
        print("Opción no válida. Por favor, elige un número válido.")
