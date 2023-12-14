import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="biblioteca",
)

mycursor = mydb.cursor()

print("Bienvenidos al sistema de consultas de biblioteca\n")

while True:
    nombre = input("¿Cuál es su Nombre?\n")
    if nombre.isalpha():
        break
    else:
        print("Por favor, ingrese solo letras. Inténtelo de nuevo.")

while True:
    print(f"\n{nombre}, ¿Quieres consultar algunas de las siguientes opciones?\n")
    print("1-Libros\n""2-Ejemplar\n""3-Historial de Prestamos\n""4-autor\n""5-usuario\n""6-Salir del programa\n")
    while True:
        try:
            num = int(input("Seleccione su opción: "))
            break
        except ValueError:
            print("Por favor, ingrese solo números. Inténtelo de nuevo.")

    if num == 1:
        print("\nLa opción que seleccionaste fue Libros\n")
        query = "SELECT * FROM Libro"
        mycursor.execute(query)
        libros = mycursor.fetchall()
        for libro in libros:
            print(libro)
        if num == 1:
            insertar = input("¿Deseas insertar un nuevo registro? (Sí/No)\n")
            if insertar.lower() == 'si':
                CodigoLibro = input("Ingrese el nuevo codigo del libro:\n")
                Titulo = input("Ingrese el titulo:\n")
                Editorial = input("Ingrese el editorial:\n")
                NumeroPaginas = input("Ingrese el numero de paginas:\n")
                CodigoAutor  = input("Ingrese el numero del autor\n")

                sql = "INSERT INTO libro (CodigoLibro, Titulo, Editorial, NumeroPaginas, CodigoAutor) VALUES (%s, %s, %s, %s, %s)"
                val = (CodigoLibro, Titulo, Editorial, NumeroPaginas, CodigoAutor)
                mycursor.execute(sql, val)
                mydb.commit()

                print("Registro insertado correctamente.")

    elif num == 2:
        print("\nLa opción que seleccionaste fue Ejemplar: \n")
        query = "SELECT * FROM Ejemplar"
        mycursor.execute(query)
        ejemplares = mycursor.fetchall()
        for ejemplar in ejemplares:
            print(ejemplar)

        insertar = input("¿Deseas insertar un nuevo registro? (Sí/No)\n")
        if insertar.lower() == 'si':
            CodigoEjemplar = input("Ingrese el id de la ejemplar:\n")
            Localizacion = input("Ingrese la Localizacion\n")
            CodigoLibro = input("Ingrese el codigo del libro:\n")
            Estado = input("Ingrese el Estado\n")

            sql = "INSERT INTO Ejemplar (CodigoEjemplar, Localizacion, CodigoLibro, Estado) VALUES (%s, %s, %s, %s)"
            val = (CodigoEjemplar, Localizacion, CodigoLibro, Estado)
            mycursor.execute(sql, val)
            mydb.commit()

            print("Registro insertado correctamente.")

    elif num == 3:
        print("\nLa opción que seleccionaste Prestamos: \n")
        query = "SELECT * FROM Prestamo"
        mycursor.execute(query)
        prestamos = mycursor.fetchall()
        for prestamo in prestamos:
            print(prestamo)

        insertar = input("¿Deseas insertar un nuevo registro? (Sí/No)\n")
        if insertar.lower() == 'si':
            CodigoPrestamo = input("Ingrese el id de el Prestamo:\n")
            FechaPrestamo = input("Ingrese la Fecha del Prestamo en el orden de AÑO/MES/DÍA.:\n")
            FechaDevolucion = input("Ingrese la Fecha de la Devolucion en el orden de AÑO/MES/DÍA.:\n")
            CodigoEjemplar = input("Ingrese el id del Ejemplar:\n")
            CodigoUsuario = input("Ingrese el codigo del Usuario\n")

            sql = "INSERT INTO Prestamo (CodigoPrestamo, FechaPrestamo, FechaDevolucion, CodigoEjemplar, CodigoUsuario) VALUES (%s, %s, %s, %s, %s)"
            val = (CodigoPrestamo, FechaPrestamo, FechaDevolucion, CodigoEjemplar, CodigoUsuario)
            mycursor.execute(sql, val)
            mydb.commit()

            print("Registro insertado correctamente.")

    elif num == 4:
        print("\nLa opción que seleccionaste fue Autor: \n")
        query = "SELECT * FROM Autor"
        mycursor.execute(query)
        autores = mycursor.fetchall()
        for autor in autores:
            print(autor)

        insertar = input("¿Deseas insertar un nuevo registro? (Sí/No)\n")
        if insertar.lower() == 'si':
            CodigoAutor = input("Ingrese el id el Autor:\n")
            NombreAutor = input("Ingrese el Nombre del autor\n")

            sql = "INSERT INTO Autor (CodigoAutor, NombreAutor) VALUES (%s, %s)"
            val = (CodigoAutor, NombreAutor)
            mycursor.execute(sql, val)
            mydb.commit()

            print("Registro insertado correctamente.")

    elif num == 5:
        print("\nLa opción que seleccionaste fue Usuario: \n")
        query = "SELECT * FROM Usuario"
        mycursor.execute(query)
        usuarios = mycursor.fetchall()
        for usuario in usuarios:
            print(usuario)

        insertar = input("¿Deseas insertar un nuevo registro? (Sí/No)\n")
        if insertar.lower() == 'si':
            CodigoUsuario = input("Ingrese el id del usuario:\n")
            NombreUsuario = input("Ingrese su nombre\n")
            Direccion = input("Ingrese su direccion:\n")
            Telefono  = input("Ingrese el telefono\n")

            sql = "INSERT INTO Usuario (CodigoUsuario, NombreUsuario, Direccion, Telefono) VALUES (%s, %s, %s, %s)"
            val = (CodigoUsuario, NombreUsuario, Direccion, Telefono)
            mycursor.execute(sql, val)
            mydb.commit()

            print("Registro insertado correctamente.")

    elif num == 6:
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Por favor, elige un número válido.")

mycursor.close()
mydb.close()